import subprocess
import os
from app_control import control as ctrl
import webbrowser as wb


def check_app_mac(app):
    app_path = f"/Applications/{app}.app"

    if os.path.exist(app_path):
        return True
    return False

def protocol(command):
    command= command.removeprefix("protocol ").strip() # for ex "coding"
    #check the json for what apps to open and what apps to close.
    if command == "coding":
        ctrl("vscode")
        ctrl("terminal")
        if check_app_mac("ChatGPT Classic.app"):
            ctrl("chatgpt")
        else:
            wb.open("https://chatgpt.com")
        wb.open("https://github.com")
        wb.open("https://hackatime.hackclub.com")
        if check_app_mac("Spotify.app"):
            ctrl("spotify")
        else:
            wb.open("https://open.spotify.com")
        return "Coding Protocol Active"


        
        
    elif command == "study":
        # open chatgpt, claude, anyhting, turn on pririty mode
        pass
    elif command == "house party":
        #trun evrythign off an amek the enjoy message and silence my computer turn of do not disturb mode
        pass
    elif command == "clean state":
        # make the comp ready for shutdwon close all the applciationsa and that yp e of way
        pass

    else:
        return "Protocol not found, go to settings -> protocols -> add-custom-protocol. \nHere type out in own words what should happen and it will be added to your protocol list. \n Wait! now for better results restart the cli and carry on."
