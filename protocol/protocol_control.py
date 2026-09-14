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
        script = """
        tell application "Safari"
            set distracting_sites to {"""" + '", "'.join(entertaining_applications) + """"}
            
            repeat with w in windows
                repeat with t in tabs of w
                    set tab_url to URL of t
                    repeat with site in distracting_sites
                        if tab_url contains site then
                            close t
                            exit repeat
                        end if
                    end repeat
                end repeat
            end repeat
        end tell
        """

        try:
            # Use subprocess.run to execute the osascript
            result = subprocess.run(
                ["osascript", "-e", script], 
                capture_output=True, 
                text=True, 
                check=True
            )
            print("Successfully closed distracting tabs.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to close tabs: {e.stderr}")


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
        return "Coding Protocol ACTIVE"


        
        
    elif command == "study":
        


    elif command == "house party":
        #trun evrythign off an amek the enjoy message and silence my computer turn of do not disturb mode
        pass
    elif command == "clean state":
        # make the comp ready for shutdwon close all the applciationsa and that yp e of way
        pass

    else:
        return "Protocol not found, go to settings -> protocols -> add-custom-protocol. \nHere type out in own words what should happen and it will be added to your protocol list. \n Wait! now for better results restart the cli and carry on."
