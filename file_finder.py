import os
import subprocess

def find_files(query):
    filename = query.removeprefix("find ").strip().lower()
    if not filename:
        print("Enter a filename. Ex: find homework")
        return

    home = os.path.expanduser('~')
    # will only search desktop, downloads and docs
    places = [
        os.path.join(home, "Desktop"),
        os.path.join(home, "Documents"),
        os.path.join(home, "Downloads")
    ]

    matches = []
    for folder in places:
        if not os.path.exists(folder):
            continue

        for current_folder, subfolder, files in os.walk(folder):
            subfolder[:] = [
                folder_name
                for folder_name in subfolder
                if not folder_name.startswith(".")
                and folder_name not in ["node_modules", ".git"]
            ]

            for file_name in files:
                if filename in file_name.lower():
                    full_path = os.path.join(current_folder, file_name)
                    matches.append(full_path)
                    

    if not matches:
        print("NO matches")
    else:
        print(matches[:20])
        for number, path in enumerate(matches, start=1):
            print(f'{number}. path')

            try:
                choice = int(input("Open which file. Enter 0 to cancel: "))

                if choice == 0:
                    return

                selected_file = matches[choice - 1]
                subprocess.run(["open", selected_file])
                print("File opened")
            except (ValueError, IndexError):
                print("Invalid choice.")

    # get the whole ls of deskto