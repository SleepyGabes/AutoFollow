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
# Version 1.0.6
# Contributors: Sirvoid, Rexac, Outsider, Wardergrip
# Credit to mage/sage343 on Discord for the new logo!
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
import requests
import json

pyautogui.PAUSE = 0.5
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'
last_target = "last_target.txt"

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
        self.master.iconbitmap("images/af.ico")

        # Load the image
        image_path = "images/afimg.png"  # Update with your image file path
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
            self.input_window.geometry("300x100")
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
        self.input_window.destroy()



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


# Function to get a server list from dashlistapi (Outsider Code)
def get_server_list():
    response = requests.get('https://dashlistapi.hyperdash.dev/')
    if response.status_code == 200:
        return json.loads(response.text).values()
    else:
        print("ERROR: UNABLE TO REACH dashlistapi.hyperdash.dev")

# Function for finding the player by the dashlistapi (Outsider Code)
def get_server_by_player(server_list, player_to_find):
    for server in server_list:
        player = get_player_details(server, player_to_find)
        if(player is not None):
            print(f"Found {player_to_find} in lobby {server['name']}")
            return server
    print(f"ERROR: Player {player_to_find} is not online.")

# Function for Name and Clan Tag (Outsider Code)
def get_player_details(server, player_to_find):
    for player in server['players']:
        if player['name'].lower() == player_to_find.lower():
            return player

# Function to join server (Outsider)
def JoinServer(server_name):
    global inlobby
    pyautogui.click(1145, 565)  # Server Browser
    pyautogui.click(x=850, y=645)  # Click Server Search box
    pyautogui.typewrite(server_name)  # Server search
    time.sleep(0.5)
    pyautogui.click(845, 495)  # Click Server in list
    pyautogui.click(1075, y=710)  # Click Join Game Button
    wait_for_black_alternation(0, 0)  # Load into lobby
    inlobby = True

# Function for pause when screen goes black a.k.a Loading Scenes. (Outsider Code)
def wait_for_black_alternation(x_offset = 0, y_offset = 0):
    print("Waiting for game to load")
    while (True):
        if(pyautogui.pixelMatchesColor(x_offset, y_offset, (0,0,0))):
            while(True):
                if(not pyautogui.pixelMatchesColor(x_offset, y_offset, (0,0,0))):
                    print("Game loaded")
                    return
                time.sleep(0.1)
        time.sleep(0.1)

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
    text = pytesseract.image_to_string(image, config='--psm 7 --oem 1 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!.,$_\\\'\\\"" "').strip() # More accurate reading for Tesseract
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
    activate_window()
    time.sleep(2)
    # Main loop for the script
    while True:
        if inlobby:
            check_for_player()
        if not inlobby:
            time.sleep(2)
            server_list = get_server_list()
            server = get_server_by_player(server_list, target)
            if server:
                JoinServer(server["name"])
            time.sleep(15)


if __name__ == "__main__":
    main()
