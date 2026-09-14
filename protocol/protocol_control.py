import subprocess

def protocol(command):
    command= command.removeprefix("protocol ").strip() # for ex "coding"
    #check the json for what apps to open and what apps to close.
    if command == "coding":
            #open vs code, chatpgt app if available, else chat on safari, spotify app or web, terminal, github.com, hackatime.com, anythhingi remeber
        pass
    elif command == "study":
        # open chatgpt, claude, anyhting, turn on pririty mode
        pass
    elif command == "house party":
        #trun evrythign off an amek the enjoy message and silence my computer turn of do not disturb mode
        pass
    elif command == "clean state":
        # make the comp ready for shutdwon close all the applciationsa and that yp e of way
        pass

    return "Protocol not found, go to settings -> protocols -> add-custom-protocol. \nHere type out in own words what should happen and it will be added to your protocol list. \n Wait! now for better results restart the cli and carry on."
