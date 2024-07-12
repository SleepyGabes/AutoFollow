import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import PhotoImage
from pynput import mouse
import threading


class MouseLoggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Follows Click Logger")
        self.root.iconbitmap("images/af.ico")  # Path to icon file

        self.label = tk.Label(self.root, text="Welcome to Auto Follows Click Logger!", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        image_path = "images/afimg.png"  # Path to image file
        self.image = PhotoImage(file=image_path)
        self.image_label = tk.Label(root, image=self.image)
        self.image_label.pack()

        self.text_area = ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.control_button = tk.Button(root, text="Stop Listening", command=self.toggle_listening)
        self.control_button.pack(pady=5)

        self.dump_button = tk.Button(root, text="Dump Logs to File", command=self.dump_logs)
        self.dump_button.pack(pady=5)

        self.listener = None
        self.is_listening = True
        self.start_logging()

    def start_logging(self):
        # Start the mouse listener in a separate thread to avoid blocking the GUI
        threading.Thread(target=self.start_mouse_listener, daemon=True).start()

    def start_mouse_listener(self):
        def on_click(x, y, button, pressed):
            if pressed:
                log_message = f"Mouse clicked at position: ({x}, {y})"
                self.log(log_message)

        self.listener = mouse.Listener(on_click=on_click)
        self.listener.start()
        self.log("Mouse listener started. Click anywhere on the screen to see the mouse position.")
        self.listener.join()

    def stop_listening(self):
        if self.listener:
            self.listener.stop()
            self.log("Mouse listener stopped.")

    def toggle_listening(self):
        if self.is_listening:
            self.stop_listening()
            self.control_button.config(text="Start Listening")
        else:
            self.start_logging()
            self.control_button.config(text="Stop Listening")
        self.is_listening = not self.is_listening

    def log(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)  # Scroll to the end to show the latest message

    def dump_logs(self):
        logs = self.text_area.get("1.0", tk.END)
        with open("console_output.log", "w") as log_file:
            log_file.write(logs)
        self.log("Logs dumped to console_output.log")

def main():
    root = tk.Tk()
    gui = MouseLoggerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
