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
# Version 1.0.8
# Contributors: Sirvoid, Rexac, Outsider, Wardergrip
# Credit to mage/sage343 on Discord for the new logo!
# You can find updates of the mod here!
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# GitHub: https://github.com/SleepyGabes
# Discord Server: https://discord.gg/FFGukgu98K
# Modify the mod to your liking, just make sure you put me in the credits as the original source!
# Thank you, enjoy using AutoFollow!
# PS: This is my first time coding a script, so excuse my "logical order", or if it doesn't make sense.

import tkinter as tk
import webbrowser
from tkinter import messagebox
from tkinter import PhotoImage
import time
import pyautogui
import pygetwindow
import pygetwindow as gw
import pytesseract
from PIL import Image
from sys import exit
import requests
import json
import subprocess

inlobby = False  # Beginning statement so that it doesn't automatically check for players at the top.
pyautogui.PAUSE = 0.5  # Pause for 0.5 in between interactions
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'  # Tesseract-OCR

with open('config.json', 'r') as file:
    config = json.load(file)

slot_regions = config['slot_regions']  # Defined slot regions
open_hd = config['path_to_hd']
p_target = 'p_target.txt'  # Defined p_target

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

# Auto Follow GUI class
class AFGUI:
    def __init__(self, AF):
        self.root = AF
        self.root.title("Auto Follow")
        self.root.iconbitmap("images/af.ico")  # Path to icon file

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.onquit)
        self.filemenu.add_command(label="Close Without Question", command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Open config file", command=self.open_config)
        self.filemenu.add_command(label="Open read me file", command=self.open_readme)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Discord Server", command=self.open_discord_invite)

        self.menubar.add_cascade(menu=self.filemenu, label="Options")

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Welcome to Auto Follow!", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        image_path = "images/afimg.png"  # Path to image file
        self.image = PhotoImage(file=image_path)
        self.image_label = tk.Label(AF, image=self.image)
        self.image_label.pack()

        self.target = tk.Button(self.root, text="Set new target", font=('Arial', 14), command=self.f_target)
        self.target.pack(padx=5, pady=5)

        self.p_target = tk.Button(self.root, text="Use previous target: " + read_file(p_target), font=('Arial', 14), command=self.p_target)
        self.p_target.pack(padx=5, pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.onquit)

    def onquit(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
            exit()

    def f_target(self):
        global target
        self.input_window = tk.Tk()  # Create a new window for input
        self.input_window.title("Enter Target")
        self.input_window.geometry("300x100")
        self.input_label = tk.Label(self.input_window, text="Enter the target's name:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self.input_window)
        self.input_entry.pack()
        self.input_button = tk.Button(self.input_window, text="Submit", command=self.get_input)
        target = read_file(p_target)
        self.input_button.pack()

    def p_target(self):
        global target
        target = read_file(p_target)
        self.root.destroy()

    def get_input(self):
        global target
        global p_target
        target = self.input_entry.get()
        write_file(p_target, target)
        self.input_window.destroy()
        self.root.destroy()
        # self.p_target.config(text="Use previous target: " + target)

    def open_config(self):
        subprocess.Popen(r'notepad config.json')

    def open_readme(self):
        subprocess.Popen(r'notepad README.md')

    def open_discord_invite(self):
        webbrowser.open_new('https://discord.gg/FFGukgu98K')

# Auto Open class
class AutoOpen:
    # Check if to auto open Hyper Dash
    @classmethod
    def auto_open_hd(self):
        path_to_hd = config['path_to_hd']
        auto_open_hd = config['auto_open_hd']
        args = ["-vrmode None", "-novr"]

        if auto_open_hd == False:
            print("Auto Open Hyper Dash feature is turned off, check your config.json settings. Continuing script...")
        elif True:
            print("Opening Hyper Dash.")
            subprocess.Popen([path_to_hd] + args)

    # Check if to auto open OBS Studio
    @classmethod
    def auto_open_obs(self):
        path_to_obs = config['path_to_obs']
        auto_open_obs = config['auto_open_obs']

        if auto_open_obs == False:
            print("Auto Open OBS feature is turned off, check your config.json settings. Continuing script...")
        elif True:
            print("Opening OBS.")
            subprocess.Popen([path_to_obs])

# Auto Follow class
class AutoFollow:
    # Switching to Hyper Dash
    @classmethod
    def activate_window(self):
        try:
            windows = gw.getWindowsWithTitle("Hyper Dash")
            for window in windows:
                window.activate()
                print("Switching to Hyper Dash")
        except pygetwindow.PyGetWindowException:
            print("Unable to find to find Hyper Dash window! Stopping program.")
            input()
            exit()


    # Function to get a server list from dashlistapi (Outsider Code)
    @classmethod
    def get_server_list(self):
        response = requests.get('https://dashlistapi.hyperdash.dev/')
        if response.status_code == 200:
            return json.loads(response.text).values()
        else:
            print("ERROR: UNABLE TO REACH dashlistapi.hyperdash.dev")

    # Function for finding the player by the dashlistapi (Outsider Code)
    @classmethod
    def get_server_by_player(self, server_list, player_to_find):
        for server in server_list:
            player = self.get_player_details(server, player_to_find)
            if(player is not None):
                print(f"Found {player_to_find} in lobby {server['name']}")
                return server
        print(f"ERROR: Player {player_to_find} is not online.")

    # Function for Name and Clan Tag (Outsider Code)
    @classmethod
    def get_player_details(self, server, player_to_find):
        for player in server['players']:
            if player['name'].lower() == player_to_find.lower():
                return player

    # Function to join server (Outsider)
    @classmethod
    def JoinServer(self, server_name):
        global inlobby
        pyautogui.click(config['server_browser'])  # Server Browser
        pyautogui.click(config['server_search'])  # Click Server Search box
        pyautogui.typewrite(server_name)  # Typing Server Name
        time.sleep(0.5)
        pyautogui.click(config['server_list'])  # Click Server in list
        pyautogui.click(config['join_game'])  # Click Join Game Button
        self.wait_for_black_alternation()  # Load into lobby
        time.sleep(0.5)
        inlobby = True

    # Function for pause when screen goes black a.k.a Loading Scenes. (Outsider Code)
    @classmethod
    def wait_for_black_alternation(self, x_offset=1075, y_offset=710):
        print("Waiting for game to load")
        while (True):
            if(pyautogui.pixelMatchesColor(x_offset, y_offset, (0,0,0))):
                while(True):
                    if(not pyautogui.pixelMatchesColor(x_offset, y_offset, (0,0,0))):
                        print("Game loaded")
                        return
                    time.sleep(0.1)
            time.sleep(0.1)

    # Check's to see if the game loaded
    @classmethod
    def check_game_loaded(self):
        skins_ad = config["skins_ad"]
        self.wait_for_black_alternation(x_offset=1075, y_offset=710)
        time.sleep(1.5)
        pyautogui.click(skins_ad)

    # Save the slot images
    @classmethod
    def save_slot_images(self):
        for i, region in enumerate(slot_regions, start=1):
            slot_img = pyautogui.screenshot(region=region)
            # Convert to grayscale
            slot_img = slot_img.convert('L')
            slot_img.save(f"images/slot{i % 10}.png")


    # Function to read text from image using pytesseract
    @classmethod
    def read_text_from_image(self, image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, config='--psm 7 --oem 1 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789?!.,$_\\\'\\\"" "').strip() # More accurate reading for Tesseract
        print(text)  # Debugging purposes
        return text.strip()


    # Function to leave the lobby
    @classmethod
    def leaving_lobby(self):
        global inlobby
        print("Player was not found! Leaving lobby.")
        pyautogui.press("tab")
        pyautogui.moveTo(config["leave_game"])
        pyautogui.click()
        inlobby = False
        time.sleep(10)  # Cooldown for checking if the player is online


    # Function to check for player's name
    @classmethod
    def check_for_player(self):
        global inlobby
        player_name = target  # Replace with the player's name you're looking for
        try_amount = 0
        try_int = config['try_int']

        # Loop through slots to check for player's name
        while try_amount < try_int:  # New Condition
            self.save_slot_images()
            # Loop through slots to check for player's name
            for i, region in enumerate(slot_regions, start=1):
                image_path = f"images/slot{i % 10}.png"
                text = self.read_text_from_image(image_path)
                if player_name in text:
                    pyautogui.press(str(i % 10))
                    print(f"Player found in slot {i % 10}. Pressed key {i % 10}.")
                    time.sleep(10)  # Wait for 10 seconds before rechecking
                    return  # Exit function if player found
                else:
                    try_amount += 1
            try_amount -= 9
            print(f"Haven't found player yet. The try amount is: {try_amount}. At {try_int} the drone will leave the lobby.")
            time.sleep(2)
        # If player not found within 10 seconds
        if try_amount >= try_int:
            self.leaving_lobby()

# Main operation for Auto Follow
def main():
    root = tk.Tk()
    app = AFGUI(root)
    root.geometry("300x300")
    root.mainloop()
    time.sleep(5)
    AutoOpen.auto_open_obs()
    AutoOpen.auto_open_hd()
    AutoFollow.check_game_loaded()
    time.sleep(10)
    AutoFollow.activate_window()
    time.sleep(2)
    # Main loop for the script
    while True:
        if inlobby:
            AutoFollow.check_for_player()
        if not inlobby:
            time.sleep(2)
            server_list = AutoFollow.get_server_list()
            server = AutoFollow.get_server_by_player(server_list, target)
            if server:
                AutoFollow.JoinServer(server["name"])
            time.sleep(15)


if __name__ == "__main__":
    main()
