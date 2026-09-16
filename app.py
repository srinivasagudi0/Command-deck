from help import help
from datetime import datetime
import random
from app_control import control as ctrl
from system_scan import scan
from protocol.protocol_control import protocol as pt
from settings.setting_control import settings, load_settings, theme_code
from file_finder import find_files as finds

while True:
    color = theme_code(load_settings())
    command = input(f"{color}> \033[0m").lower().strip()

    if command == "commands":
        print(help())

    elif command == "exit":
        break

    elif command == "settings":
        settings()

    elif command=="time":
        now = datetime.now()
        print(now.strftime("%I:%M %p"))
    elif command =="coin":
        side = random.choice(["heads", "tails"])
        print(side)

    elif command.startswith("open") or command.startswith("launch"):
        ctrl(command)
    elif command == "scan" or command =="check" or command =="health":
        scan()
    elif command.startswith("protocol "):
        print(pt(command))

    elif command.startswith("find ")
    else:
        print("Unknown Command")
