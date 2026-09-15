import json

def settings():

    with open("settings/seetings.json", "r") as f:
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

            

        elif choice == 3:
            print("1. Classic")
            print("2. CyberPunk")
            print("3. Choose a color")
            print("4. Weight of the theme")
        elif choice == 4:
            break
        else:
            continue
