import os

def find_files(query):
    filename = query.removeprefix("find ").strip().lower()
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
                    if len(matches) >= 20:
                        return matches

    if not matches:
        print("NO matches")
        print(matches)


    # get the whole ls of deskto