import json

def settings():

    with open("settings/settings.json", "r") as f:
        data = json.load(f)

    while True:
        print("Type a number to select")
        print("1. General")
        print("2. Protocol")
        print("3. Theme")
        print("4. exit")

        while True:
            try:
                choice = int(input("Type a choice > "))
                break
            except:
                print("Choose between 1,2,3,4")
                continue

        if choice == 1:
            print("1. Change User Name")
            print("2. Toggle confirm Before Closing application")
            print("3. Back")

            general_choice = input("Setting: ").strip()

            if general_choice == "1":
                new_name = input("Enter a new user name: ").strip()

                if new_name:
                    data["general"]["user_name"] = new_name

                    with open("settings/settings.json", "w") as s:
                        json.dump(data, s, indent=4)

                    print("User name changed.")

            elif general_choice == "2":
                current = data["general"]['confirm_before_closing']
                data["general"]["confirm_before_closing"] = not current

                with open('settings/settings.json', 'w') as file:
                    json.dump(data, file, indent=4)

                print(
                    "Confirm before closing: ",
                    data["general"]["confirm_before_closing"]
                )

            elif general_choice == "3":
                continue
            else:
                print("Invalid Choice")
                        
        elif choice == 2:
            print("1.Coding protocol")
            print("2. Study protocol")
            print("3. Clean State protocol")
            print("4. Add a new protocol!")
            print("5. Back")

            protocol_choice = input("settings: ").strip()

            if protocol_choice =="1":
                coding = data["protocols"]["coding"]

                options = [
                    ("VS Code", "vscode"),
                    ("Terminal", "terminal"),
                    ("ChatGPT", "chatgpt"),
                    ("GitHub", "github"),
                    ("Hackatime", "hackatime"),
                    ("Spotify", "spotify")
                ]

                while True:
                    print("\nCoding Protocol Settings")
                    for number, option in enumerate(options, start=1):
                        label = option[0]
                        key = option[1]
                        status = "ON" if coding[key] else "OFF"
                        print(f"{number}. {label}: {status}")
                    print("7. Back")

                    coding_choice = input("> ").strip()

                    if coding_choice == "7":
                        break

                    if coding_choice.isdigit():
                        number = int(coding_choice)

                        if 1 <= number <=6:
                            key = options[number - 1][1]
                            coding[key] = not coding[key]

                            with open("settings/settings.json", "w") as file:
                                json.dump(data, file, indent=4)

                            print("Setting Updated")
                        else:
                            print("Choose between 1 and 7. ")
                    else:
                        print("enter a number")
            elif protocol_choice == "5":
                continue
            else:
                print("That section is coming next. ")

            

        elif choice == 3:
            print("1. Classic")
            print("2. CyberPunk")
            print("3. Choose a color")
            print("4. Weight of the theme")
        elif choice == 4:
            break
        else:
            continue
