from help import help
from datetime import datetime
import random
import math

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

                 
            

        


    else:
        print("Unknown Command")
        