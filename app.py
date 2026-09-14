from help import help
from datetime import datetime
import random
from app_control import control as ctrl
from system_scan import scan

while True:
    command = input("> ").lower()

    if command == "commands":
        print(help())

    elif command == "exit":
        exit()

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




        


    else:
        print("Unknown Command")
        