# ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗        ████████╗░█████╗░
# ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝        ╚══██╔══╝██╔══██╗
# ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░        ░░░██║░░░██║░░██║
# ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░        ░░░██║░░░██║░░██║
# ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗        ░░░██║░░░╚█████╔╝
# ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝        ░░░╚═╝░░░░╚════╝░
#
# ░█████╗░██╗░░░██╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗
# ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║
# ███████║██║░░░██║░░░██║░░░██║░░██║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝
# ██╔══██║██║░░░██║░░░██║░░░██║░░██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░
# ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░
# ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░

# This program was written by SleepyGabes on GitHub!
# Version 1.0.5
# Contributors: Sirvoid, Rexac
# Credit to mage/sage343 on Discord for the new logo!
# Credits for troubleshooting to Outsider
# You can find updates of the mod here!
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# GitHub: https://github.com/SleepyGabes
# Discord Server: https://discord.gg/FFGukgu98K
# Modify the mod to your liking, just make sure you put me in the credits as the original source!
# Thank you, enjoy using AutoFollow!
# PS: This is my first time coding a script, so excuse my "logical order", or if it doesn't make sense.

import time
import pyautogui
import pygetwindow
import pygetwindow as gw
import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import PhotoImage
from sys import exit

pytesseract.pytesseract.tesseract_cmd = '_internal/Tesseract-OCR/tesseract.exe'
last_target = "_internal/last_target.txt"
# Defined slot regions
slot_regions = [
    (87, 30, 131, 28),
    (229, 30, 131, 28),
    (371, 30, 131, 28),
    (513, 30, 131, 28),
    (655, 30, 131, 28),
    (1134, 30, 131, 28),
    (1276, 30, 131, 28),
    (1418, 30, 131, 28),
    (1560, 30, 131, 28),
    (1702, 30, 131, 28)
]

# Beginning statement so that it doesn't automatically check for players at the top.
inlobby = False


def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    # print(f"Content written to '{file_name}' successfully.")


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None


# Prompt the user to specify their target
class MultipleChoiceWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("AutoFollow")

        # Change window icon
        self.master.iconbitmap("_internal/images/af.ico")

        # Load the image
        image_path = "_internal/images/afimg.png"  # Update with your image file path
        self.image = PhotoImage(file=image_path)

        # Create a label widget to display the image
        self.image_label = tk.Label(master, image=self.image)
        self.image_label.pack()

        self.question_label = tk.Label(master, text="Welcome to AutoFollow!")
        self.question_label.pack()
        self.question_label = tk.Label(master, text="What would you like to do?")
        self.question_label.pack()

        self.var = tk.StringVar()

        self.radio_button1 = tk.Radiobutton(master, text="Set new target.", variable=self.var, value="1")
        self.radio_button1.pack(anchor='w')
        self.var.set("1")

        target = read_file(last_target)
        self.radio_button2 = tk.Radiobutton(master, text="Use previous target. " + "(" + target + ")", variable=self.var, value="2")
        self.radio_button2.pack(anchor='w')
        self.var.set("2")

        self.radio_button3 = tk.Radiobutton(master, text="Exit AutoFollow", variable=self.var, value="3")
        self.radio_button3.pack(anchor='w')
        self.var.set("3")

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_button.pack()

    def submit_answer(self):
        global target
        global last_target
        answer = self.var.get()
        if answer == "1":
            self.master.destroy()  # Close the main window
            self.input_window = tk.Tk()  # Create a new window for input
            self.input_window.title("Enter Target")
            self.input_label = tk.Label(self.input_window, text="Enter the target's name:")
            self.input_label.pack()
            self.input_entry = tk.Entry(self.input_window)
            self.input_entry.pack()
            self.input_button = tk.Button(self.input_window, text="Submit", command=self.get_input)
            target = read_file(last_target)
            self.input_button.pack()
        elif answer == "2":
            target = read_file(last_target)
            self.master.destroy()
            return target
        elif answer == "3":
            self.master.destroy()
            exit()

    def get_input(self):
        global target
        global last_target
        target = self.input_entry.get()
        write_file(last_target, target)



# Switching to Hyper Dash
def activate_window():
    try:
        windows = gw.getWindowsWithTitle("Hyper Dash")
        for window in windows:
            window.activate()
            print("Switching to Hyper Dash")
    except pygetwindow.PyGetWindowException:
        taskbar = pyautogui.locateCenterOnScreen('_internal/images/hd.png', confidence=0.85)
        pyautogui.click(taskbar)


# Defined the join button
def joinbutton():
    global inlobby
    try:
        joinbutton = pyautogui.locateCenterOnScreen('_internal/images/join.png', confidence=0.85)
        if joinbutton:
            pyautogui.moveTo(630, 494)
            pyautogui.click()
            time.sleep(5)
            print("Join button is available right now. Attempting to join lobby.")
            time.sleep(4)
            inlobby = True
        else:
            print("Join button not available right now.")
            time.sleep(3)
    except pyautogui.ImageNotFoundException:
        print("Join button not found.")
        time.sleep(3)


# Save the slot images
def save_slot_images():
    for i, region in enumerate(slot_regions, start=1):
        slot_img = pyautogui.screenshot(region=region)
        slot_img.save(f"_internal/images/slot{i % 10}.png")
        # Convert to grayscale
        slot_img = slot_img.convert('L')
        slot_img.save(f"_internal/images/slot{i % 10}.png")


# Function to read text from image using pytesseract
def read_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print(text)  # Debugging purposes
    return text.strip()


# Function to leave the lobby
def leaving_lobby():
    global inlobby
    print("Player was not found! Leaving lobby.")
    pyautogui.press("tab")
    pyautogui.moveTo(645, 318)
    pyautogui.click()
    inlobby = False
    # Checking again in
    time.sleep(10)


# Function to check for player's name
def check_for_player():
    global inlobby
    player_name = target  # Replace with the player's name you're looking for
    try_amount = 0

    # Loop through slots to check for player's name
    while try_amount < 3:  # New Condition
        save_slot_images()
        # Loop through slots to check for player's name
        for i, region in enumerate(slot_regions, start=1):
            image_path = f"_internal/images/slot{i % 10}.png"
            text = read_text_from_image(image_path)
            if player_name in text:
                pyautogui.press(str(i % 10))
                print(f"Player found in slot {i % 10}. Pressed key {i % 10}.")
                return  # Exit function if player found
            else:
                try_amount += 1
                # print(f"Trying {try_amount}.")
        try_amount -= 9
        time.sleep(10)  # Wait for 10 seconds before rechecking

    # If player not found within 10 seconds
    if try_amount >= 3:
        leaving_lobby()


def main():
    root = tk.Tk()
    app = MultipleChoiceWindow(root)
    root.geometry("280x280")
    root.mainloop()
    time.sleep(5)
    # Main loop for the script
    while True:
        if inlobby:
            check_for_player()
        if not inlobby:
            joinbutton()


if __name__ == "__main__":
    main()
