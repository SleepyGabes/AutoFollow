![Image](https://imgur.com/zRomQ6G.png)

![Discord](https://img.shields.io/discord/1221883772580921344?style=for-the-badge&logo=discord&color=7289DA)

### Get started
- If you haven't already downloaded Hyper Dash on your machine head on over to either [Steam](https://store.steampowered.com/app/1386890/Hyper_Dash/) or the [Rift Store](https://www.meta.com/en-gb/experiences/pcvr/2801247513273368/) to start downloading!

- Download the latest version of Auto Follow from the [Releases](https://github.com/SleepyGabes/AutoFollow/releases).

- Unzip the contents from the zip file wherever.

- Run the executable file "`AutoFollow.exe`".

- Press "Set new target" and put your current name in Hyper Dash.
  > Without the clan tag included.

- AutoFollow will then automatically switch windows to Hyper Dash.
  > Make sure you have Hyper Dash running.

- Now join a lobby and the program will be able to follow you from lobby to lobby.
  > Sometimes you will have to manually check yourself if the program is running correctly. Because it can sometimes get stuck within the menus.

- Happy Dashing!

## Auto Open Features

If you are planning on Auto Openning Hyper Dash and OBS Studio there are few steps to follow, although these steps are **optional**.

### Step 1
First to automatically open Hyper Dash and OBS Studio, you need to get the path to them. Here are some examples:
- Hyper Dash path `C:\Oculus Downloads\Software\triangle-factory-hyper-dash\HyperDash.exe`
- OBS Studio path `C:\OBS\obs-studio\bin\64bit\obs_launch.bat`

> The reason why we aren't using the `obs64.exe` is because you will get errors so creating a custom `.bat` file will help with resolving this issue.

There are many tutorials online on how to get folder paths, so just follow one of them.

### Step 2
Second is creating the `.bat` file for OBS Studio. 
- Go to where the `obs64.exe` is located.
- Create a new **Text Document**.
- Paste the following into the **Text Document** on each new line.

`@echo off` - Turns off the console.

`cd /d "C:\OBS\obs-studio\bin\64bit"` - Path to the OBS Studio folder where the `.exe` is located.

`start obs64.exe` - Starts OBS Studio.

> Note you can add Launch Parameters to OBS, for example using this parameter: `--minimize-to-tray` will minimize OBS to tray, to find out more about OBS Studio Launch Parameteres click [here](https://obsproject.com/kb/launch-parameters).

Now after you've done that, you need to change the file type of the Text Document from `.txt` to `.bat`, this can be done through properties or if you have **File name extensions** enabled you can just change it by renaming the Text Document.

### Step 3
Third is pasting the correct paths for OBS and Hyper Dash to `config.json`, and changing both `auto_open_hd`, `auto_open_obs` to `true`.
That's it! You successfuly enabled the Auto Open Features!


## Requirements for the script to work correctly:

- Preferably 1920 x 1080p Monitor
> You can change the mouse points for the program and where to read the top scoreboard in `config.json` with the other tool `ClickLogger.exe`.

- Oculus or Steam version of Hyper Dash.

- Hyper Dash running fullscreen.

## Recommended Spectator Settings
- FOV = 90

- Spectator UI = true

- Follow on kill = false

# Note
Me and my contributors will not be liable for any malicious use, misuse, or any other inappropriate actions taken with this program. We expect everyone to use this program for the intended purpose of spectating themselves, and that it isn't used for spying other players or other malicious reasons. Thank you.
