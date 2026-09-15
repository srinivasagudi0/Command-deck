import os
from app_control import control as ctrl
import webbrowser as wb
import subprocess


def check_app_mac(app):
    app_path = f"/Applications/{app}.app"

    if os.path.exists(app_path):
        return True
    return False

def close_app(app):
    script = f'''
        if application "{app}" is running  then tell application "{app}" to quit end if
            '''
    results = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True
        )

def close_distracting_tabs():
    sites = [
        "tiktok.com",
        "youtube.com",
        "instagram.com",
        "netflix.com",
        "reddit.com"]

    site_list = ", ".join(f'"{site}"' for site in sites)

    script = f'''
    tell application "Safari"
        set distractingSites to {{{site_list}}}

        repeat with currentWindow in windows
            repeat with tabNumber from (count tabs of currentWindow) to 1 by -1
                try
                    set tabURL to URL of tab tabNumber of currentWindow

                    repeat with siteName in distractingSites
                        if tabURL contains siteName then
                            close tab tabNumber of currentWindow
                            exit repeat
                        end if
                    end repeat
                end try
            end repeat
        end repeat
    end tell
    ''' # wrote with the help of Ai

    subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )
    

def protocol(command):
    command= command.removeprefix("protocol ").strip() # for ex "coding"
    #check the json for what apps to open and what apps to close.
    if command == "coding":
        print("STARTING CODING PROTOCOL")
        ctrl("vscode")
        ctrl("terminal")
        if check_app_mac("ChatGPT Classic"):
            ctrl("chatgpt")
        else:
            wb.open("https://chatgpt.com")
        wb.open("https://github.com")
        wb.open("https://hackatime.hackclub.com")
        if check_app_mac("Spotify"):
            ctrl("spotify")
        else:
            wb.open("https://open.spotify.com")
        return "CODING protocol ACTIVE"


        
        
    elif command == "study":
        print("Starting Study Protocol")

        ctrl("safari")
        ctrl("notes")

        if check_app_mac("ChatGPT Classic"):
            ctrl("chatgpt")
        else:
            wb.open("https://chatgpt.com")

        close_choice = input("Close distracting apps or websites? (Y/n):").lower().strip()

        if close_choice in ['y', 'yes', '']:
            close_distracting_tabs()

            distracting_apps = [
                "Discord",
                "Steam",
                "TV"
            ]

            for app in distracting_apps:
                close_app(app)

            print("Distractions cleared.")
        else:
            print("Ok, I won't")
        return "STUDY protocol ACTIVE"


    elif command == "clean state":
        # make the comp ready for shutdwon close all the applciationsa and that yp e of way
        pass

    else:
        return "Protocol not found, go to settings -> protocols -> add-custom-protocol. \nHere type out in own words what should happen and it will be added to your protocol list. \n Wait! now for better results restart the cli and carry on."
