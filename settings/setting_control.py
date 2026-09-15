import json
import os

SETTINGS_PATH = os.path.join(os.path.dirname(__file__), "settings.json")

COLORS = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
def load_settings():
    with open(SETTINGS_PATH) as file:
        return json.load(file)
def save_settings(data):
    with open(SETTINGS_PATH, "w") as file:
        json.dump(data, file, indent=4)
        file.write("\n")
def theme_code(data=None):
    data = data or load_settings()
    theme = data["theme"]
    numbers = {name: number for name, number in zip(COLORS, range(30, 38))}
    color = "white"
    if theme["style"] == "cyberpunk":
        color = "magenta"
    elif theme["style"] == "custom":
        color = theme["custom_color"]
    bold = "1" if theme["bold"] or theme["style"] == "cyberpunk" else "0"
    return f"\033[{bold};{numbers[color]}m"
def toggle_settings(title, settings, data):
    keys = list(settings)
    while True:
        print("\n" + title)
        for number, key in enumerate(keys, 1):
            status = "ON" if settings[key] else "OFF"
            print(f"{number}. {key.replace('_', ' ').title()}: {status}")
        print(f"{len(keys) + 1}. Back")
        choice = input("> ").strip()
        if choice == str(len(keys) + 1):
            return
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            key = keys[int(choice) - 1]
            settings[key] = not settings[key]
            save_settings(data)
        else:
            print("Invalid choice.")
def settings():
    data = load_settings()
    while True:
        print("\n1. General\n2. Protocol\n3. Theme\n4. Exit")
        choice = input("Type a choice > ").strip()
        if choice == "1":
            print("1. Change user name\n2. Toggle confirm before closing\n3. Back")
            option = input("Setting: ").strip()
            if option == "1":
                name = input("New user name: ").strip()
                if name:
                    data["general"]["user_name"] = name
                    save_settings(data)
                else:
                    print("Name cannot be empty.")
            elif option == "2":
                current = data["general"]["confirm_before_closing"]
                data["general"]["confirm_before_closing"] = not current
                save_settings(data)
            elif option != "3":
                print("Invalid choice.")
        elif choice == "2":
            print("1. Coding\n2. Study\n3. Clean State\n4. Back")
            option = input("Setting: ").strip()
            if option == "1":
                toggle_settings("Coding Settings", data["protocols"]["coding"], data)
            elif option == "2":
                toggle_settings("Study Settings", data["protocols"]["study"], data)
            elif option == "3":
                toggle_settings("Clean State Settings", data["protocols"]["clean_state"], data)
            elif option != "4":
                print("Invalid choice.")
        elif choice == "3":
            print("1. Classic\n2. Cyberpunk\n3. Custom color\n4. Toggle bold\n5. Back")
            option = input("Setting: ").strip()
            if option in ("1", "2"):
                data["theme"]["style"] = "classic" if option == "1" else "cyberpunk"
                save_settings(data)
            elif option == "3":
                color = input("Color (" + ", ".join(COLORS) + "): ").lower().strip()
                if color in COLORS:
                    data["theme"]["style"] = "custom"
                    data["theme"]["custom_color"] = color
                    save_settings(data)
                else:
                    print("Invalid color.")
            elif option == "4":
                data["theme"]["bold"] = not data["theme"]["bold"]
                save_settings(data)
            elif option != "5":
                print("Invalid choice.")
        elif choice == "4":
            return
        else:
            print("Invalid choice.")
