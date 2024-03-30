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
# Contributors: Sirvoid, Rexac
# You can find updates of the mod here!
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# GitHub: https://github.com/SleepyGabes
# Discord Server: https://discord.gg/FFGukgu98K
# Modify the mod to your liking, just make sure you put me in the credits as the original source!
# Thank you, enjoy using AutoFollow!  PS: This is my first time coding a script, so excuse my "logical order, or if it doesn't make sense."

import time
import pyautogui
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR/tesseract.exe"

# Prompt the user to specify their target
print("Welcome to AutoFollow!")
target = input("Type the targets name: ")

# Switch to Hyper Dash
print("Target selected. Please switch to Hyper Dash now. (5 seconds to switch)")
print("To exit AutoFollow during spectating press 0.")
time.sleep(5)

# Define slot regions
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


# Save slot images
def save_slot_images():
    for i, region in enumerate(slot_regions, start=1):
        slot_img = pyautogui.screenshot(region=region)
        slot_img.save(f"images/slot{i}.png")
        # Convert to grayscale
        slot_img = slot_img.convert('L')
        slot_img.save(f"images/slot{i}.png")

# Function to read text from image using pytesseract
def read_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

# Function to check for player's name
def check_for_player():
    # Player's name
    player_name = target  # Replace with the player's name you're looking for

    # Start time for tracking 10 seconds
    start_time = time.time()

    player_found = False  # Flag to indicate whether the player has been found

    # Loop through slots to check for player's name
    while time.time() - start_time < 20:  # Check within 10 seconds
        save_slot_images()
        # Loop through slots to check for player's name
        for i, region in enumerate(slot_regions, start=1):
            image_path = f"images/slot{i}.png"
            text = read_text_from_image(image_path)
            if player_name in text:
                pyautogui.press(str(i))
                print(f"Player found in slot {i}. Pressed key {i}.")
                player_found = True
                return  # Exit function if player found
        time.sleep(10)  # Wait for 10 seconds before rechecking

    # If player not found within 10 seconds
    if not player_found:
        print("Player not found within 10 seconds. Leaving lobby.")
        pyautogui.press("tab")
        pyautogui.moveTo(645, 318)
        pyautogui.click()

        # Checking again in
        time.sleep(5)

# Main loop
while True:
    try:
        joinbutton = pyautogui.locateCenterOnScreen('images/join.png', confidence=0.75)
        if joinbutton:
            pyautogui.moveTo(630, 494)
            pyautogui.click()
            time.sleep(5)
            print("Join button is available right now. Attempting to join lobby.")
            time.sleep(4.5)
            check_for_player()
        else:
            print("Join button not available right now.")
            time.sleep(5)
    except pyautogui.ImageNotFoundException:
        print("Join button not found.")
        time.sleep(5)
