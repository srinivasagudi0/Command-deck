def control(command):
    import subprocess
    
    app = command.replace("lauch", "").replace("open", "").strip()
    result = subprocess.run(
        ["open", "-a", app],
        capture_output=True,
        text=True
    )

    if result.returncode===0:
        print(f"Opening {app}...")
    else:
        # for some apps there should be second names like, most common names, for ex, visual studio code is the name but epople claall it vs code soo.

        app_aliases = {
        # Text Editors, IDEs & Code Tools
        "vs code": "Visual Studio Code",
        "vscode": "Visual Studio Code",
        "code": "Visual Studio Code",
        "vsc": "Visual Studio Code",
        "studio code": "Visual Studio Code",
        "sublime": "Sublime Text",
        "subl": "Sublime Text",
        "st3": "Sublime Text",
        "st4": "Sublime Text",
        "intellij": "IntelliJ IDEA",
        "idea": "IntelliJ IDEA",
        "pycharm": "PyCharm",
        "webstorm": "WebStorm",
        "clion": "CLion",
        "rider": "Rider",
        "datagrip": "DataGrip",
        "phpstorm": "PhpStorm",
        "android studio": "Android Studio",
        "android": "Android Studio",
        "studio": "Android Studio",
        "xcode": "Xcode",
        "eclipse": "Eclipse",
        "netbeans": "NetBeans",
        "atom": "Atom",
        "vim": "Vim",
        "neovim": "Neovim",
        "nvim": "Neovim",
        "emacs": "Emacs",
        "notepad": "Notepad++",
        "notepadpp": "Notepad++",
        "npp": "Notepad++",
        "cursor": "Cursor",
        "zed": "Zed",

        # Web Browsers
        "chrome": "Google Chrome",
        "google chrome": "Google Chrome",
        "safari": "Safari",
        "firefox": "Mozilla Firefox",
        "ff": "Mozilla Firefox",
        "edge": "Microsoft Edge",
        "ms edge": "Microsoft Edge",
        "opera": "Opera",
        "brave": "Brave Browser",
        "arc": "Arc Browser",
        "vivaldi": "Vivaldi Browser",
        "chromium": "Chromium",

        # Terminals & Shells
        "terminal": "Terminal",
        "term": "Terminal",
        "iterm": "iTerm2",
        "iterm2": "iTerm2",
        "alacritty": "Alacritty",
        "kitty": "Kitty",
        "warp": "Warp Terminal",
        "cmd": "Command Prompt",
        "command prompt": "Command Prompt",
        "powershell": "PowerShell",
        "pwsh": "PowerShell",
        "wezterm": "WezTerm",

        # Communication & Collaboration
        "slack": "Slack",
        "teams": "Microsoft Teams",
        "ms teams": "Microsoft Teams",
        "discord": "Discord",
        "zoom": "Zoom",
        "skype": "Skype",
        "whatsapp": "WhatsApp",
        "telegram": "Telegram",
        "tg": "Telegram",
        "signal": "Signal",
        "messenger": "Facebook Messenger",
        "meet": "Google Meet",
        "webex": "Cisco Webex",

        # Productivity, Notes & Project Management
        "notion": "Notion",
        "obsidian": "Obsidian",
        "evernote": "Evernote",
        "onenote": "Microsoft OneNote",
        "linear": "Linear",
        "jira": "Jira",
        "confluence": "Confluence",
        "trello": "Trello",
        "asana": "Asana",
        "monday": "Monday.com",
        "clickup": "ClickUp",
        "todoist": "Todoist",
        "ticktick": "TickTick",

        # Design & Prototyping
        "figma": "Figma",
        "photoshop": "Adobe Photoshop",
        "ps": "Adobe Photoshop",
        "illustrator": "Adobe Illustrator",
        "ai": "Adobe Illustrator",
        "indesign": "Adobe InDesign",
        "id": "Adobe InDesign",
        "premiere": "Adobe Premiere Pro",
        "pr": "Adobe Premiere Pro",
        "after effects": "Adobe After Effects",
        "ae": "Adobe After Effects",
        "lightroom": "Adobe Lightroom",
        "lr": "Adobe Lightroom",
        "xd": "Adobe XD",
        "canva": "Canva",
        "sketch": "Sketch",
        "blender": "Blender",

        # System & Utilities
        "settings": "System Settings",
        "system settings": "System Settings",
        "pref": "System Preferences",
        "preferences": "System Preferences",
        "control panel": "Control Panel",
        "finder": "Finder",
        "explorer": "File Explorer",
        "file explorer": "File Explorer",
        "activity monitor": "Activity Monitor",
        "task manager": "Task Manager",
        "taskmgr": "Task Manager",
        "disk utility": "Disk Utility",
        "docker": "Docker Desktop",
        "docker desktop": "Docker Desktop",

        # Database Tools
        "dbeaver": "DBeaver",
        "pgadmin": "pgAdmin",
        "navicat": "Navicat",
        "tableplus": "TablePlus",
        "sequel pro": "Sequel Pro",
        "sequel ace": "Sequel Ace",
        "compass": "MongoDB Compass",

        # Developer Utilities & Git Clients
        "postman": "Postman",
        "insomnia": "Insomnia",
        "gitkraken": "GitKraken",
        "sourcetree": "Sourcetree",
        "github desktop": "GitHub Desktop",
        "github": "GitHub Desktop",

        # Music, Video & Media
        "spotify": "Spotify",
        "apple music": "Apple Music",
        "music": "Music",
        "vlc": "VLC Media Player",
        "youtube": "YouTube",
        "yt": "YouTube",
        "netflix": "Netflix",
        "obs": "OBS Studio",

        # Cloud Storage
        "drive": "Google Drive",
        "google drive": "Google Drive",
        "dropbox": "Dropbox",
        "onedrive": "Microsoft OneDrive",
        "box": "Box",
        "icloud": "iCloud",

        # Office Suites & Documents
        "word": "Microsoft Word",
        "excel": "Microsoft Excel",
        "powerpoint": "Microsoft PowerPoint",
        "ppt": "Microsoft PowerPoint",
        "outlook": "Microsoft Outlook",
        "docs": "Google Docs",
        "sheets": "Google Sheets",
        "slides": "Google Slides",
        "pages": "Pages",
        "numbers": "Numbers",
        "keynote": "Keynote"
    } # wrote with the help of AI (the dict)

        print(f"Could not find the {app}")
