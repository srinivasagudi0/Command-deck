def control(command):
    import subprocess
    
    app = command.replace("launch", "").replace("open", "").strip()
    names = {
            # Text Editors, IDEs & Code Tools
            "vs code": "Visual Studio Code.app",
            "vscode": "Visual Studio Code.app",
            "code": "Visual Studio Code.app",
            "vsc": "Visual Studio Code.app",
            "studio code": "Visual Studio Code.app",
            "sublime": "Sublime Text.app",
            "subl": "Sublime Text.app",
            "st3": "Sublime Text.app",
            "st4": "Sublime Text.app",
            "intellij": "IntelliJ IDEA.app",
            "idea": "IntelliJ IDEA.app",
            "pycharm": "PyCharm.app",
            "webstorm": "WebStorm.app",
            "clion": "CLion.app",
            "rider": "Rider.app",
            "datagrip": "DataGrip.app",
            "phpstorm": "PhpStorm.app",
            "android studio": "Android Studio.app",
            "android": "Android Studio.app",
            "studio": "Android Studio.app",
            "xcode": "Xcode.app",
            "eclipse": "Eclipse.app",
            "netbeans": "NetBeans.app",
            "atom": "Atom.app",
            "vim": "Vim.app",
            "neovim": "Neovim.app",
            "nvim": "Neovim.app",
            "emacs": "Emacs.app",
            "cursor": "Cursor.app",
            "zed": "Zed.app",
    
            # Web Browsers
            "chrome": "Google Chrome.app",
            "google chrome": "Google Chrome.app",
            "safari": "Safari.app",
            "firefox": "Mozilla Firefox.app",
            "ff": "Mozilla Firefox.app",
            "edge": "Microsoft Edge.app",
            "ms edge": "Microsoft Edge.app",
            "opera": "Opera.app",
            "brave": "Brave Browser.app",
            "arc": "Arc Browser.app",
            "vivaldi": "Vivaldi Browser.app",
            "chromium": "Chromium.app",
    
            # Terminals & Shells
            "terminal": "Terminal.app",
            "term": "Terminal.app",
            "iterm": "iTerm2.app",
            "iterm2": "iTerm2.app",
            "alacritty": "Alacritty.app",
            "kitty": "Kitty.app",
            "warp": "Warp Terminal.app",
            "powershell": "PowerShell.app",
            "pwsh": "PowerShell.app",
            "wezterm": "WezTerm.app",
    
            # Communication & Collaboration
            "slack": "Slack.app",
            "teams": "Microsoft Teams.app",
            "ms teams": "Microsoft Teams.app",
            "discord": "Discord.app",
            "zoom": "Zoom.app",
            "skype": "Skype.app",
            "whatsapp": "WhatsApp.app",
            "telegram": "Telegram.app",
            "tg": "Telegram.app",
            "signal": "Signal.app",
            "messenger": "Facebook Messenger.app",
            "meet": "Google Meet.app",
            "webex": "Cisco Webex.app",
    
            # Productivity, Notes & Project Management
            "notion": "Notion.app",
            "obsidian": "Obsidian.app",
            "evernote": "Evernote.app",
            "onenote": "Microsoft OneNote.app",
            "linear": "Linear.app",
            "jira": "Jira.app",
            "confluence": "Confluence.app",
            "trello": "Trello.app",
            "asana": "Asana.app",
            "monday": "Monday.com.app",
            "clickup": "ClickUp.app",
            "todoist": "Todoist.app",
            "ticktick": "TickTick.app",
    
            # Design & Prototyping
            "figma": "Figma.app",
            "photoshop": "Adobe Photoshop.app",
            "ps": "Adobe Photoshop.app",
            "illustrator": "Adobe Illustrator.app",
            "ai": "Adobe Illustrator.app",
            "indesign": "Adobe InDesign.app",
            "id": "Adobe InDesign.app",
            "premiere": "Adobe Premiere Pro.app",
            "pr": "Adobe Premiere Pro.app",
            "after effects": "Adobe After Effects.app",
            "ae": "Adobe After Effects.app",
            "lightroom": "Adobe Lightroom.app",
            "lr": "Adobe Lightroom.app",
            "xd": "Adobe XD.app",
            "canva": "Canva.app",
            "sketch": "Sketch.app",
            "blender": "Blender.app",
    
            # macOS System & Utilities
            "settings": "System Settings.app",
            "system settings": "System Settings.app",
            "pref": "System Settings.app",
            "preferences": "System Settings.app",
            "finder": "Finder.app",
            "activity monitor": "Activity Monitor.app",
            "disk utility": "Disk Utility.app",
            "docker": "Docker.app",
            "docker desktop": "Docker.app",
    
            # Database Tools
            "dbeaver": "DBeaver.app",
            "pgadmin": "pgAdmin.app",
            "navicat": "Navicat.app",
            "tableplus": "TablePlus.app",
            "sequel pro": "Sequel Pro.app",
            "sequel ace": "Sequel Ace.app",
            "compass": "MongoDB Compass.app",
    
            # Developer Utilities & Git Clients
            "postman": "Postman.app",
            "insomnia": "Insomnia.app",
            "gitkraken": "GitKraken.app",
            "sourcetree": "Sourcetree.app",
            "github desktop": "GitHub Desktop.app",
            "github": "GitHub Desktop.app",
    
            # Music, Video & Media
            "spotify": "Spotify.app",
            "apple music": "Apple Music.app",
            "music": "Music.app",
            "vlc": "VLC Media Player.app",
            "youtube": "YouTube.app",
            "yt": "YouTube.app",
            "netflix": "Netflix.app",
            "obs": "OBS Studio.app",
    
            # Cloud Storage
            "drive": "Google Drive.app",
            "google drive": "Google Drive.app",
            "dropbox": "Dropbox.app",
            "onedrive": "Microsoft OneDrive.app",
            "box": "Box.app",
            "icloud": "iCloud.app",
    
            # Office Suites & Documents
            "word": "Microsoft Word.app",
            "excel": "Microsoft Excel.app",
            "powerpoint": "Microsoft PowerPoint.app",
            "ppt": "Microsoft PowerPoint.app",
            "outlook": "Microsoft Outlook.app",
            "docs": "Google Docs.app",
            "sheets": "Google Sheets.app",
            "slides": "Google Slides.app",
            "pages": "Pages.app",
            "numbers": "Numbers.app",
            "keynote": "Keynote.app",
    
            # Password Managers & Security
            "1password": "1Password.app",
            "1p": "1Password.app",
            "bitwarden": "Bitwarden.app",
            "bw": "Bitwarden.app",
            "keepass": "KeePass.app",
            "protonvpn": "Proton VPN.app",
            "proton vpn": "Proton VPN.app",
            "nord": "NordVPN.app",
            "nordvpn": "NordVPN.app",
    
            # AI Native Clients
            "chatgpt": "ChatGPT.app",
            "gpt": "ChatGPT.app",
            "claude": "Claude.app",
            "ollama": "Ollama.app",
    
            # Specialized Mac Utilities
            "raycast": "Raycast.app",
            "alfred": "Alfred.app",
            "rectangle": "Rectangle.app",
            "snagit": "Snagit.app",
            "localsend": "LocalSend.app",
    
            # Gaming & Entertainment
            "steam": "Steam.app",
            "epic": "Epic Games Launcher.app",
            "battlenet": "Battle.net.app",
            "bnet": "Battle.net.app",
            "gog": "GOG Galaxy.app",
    
            # Miscellaneous Productivity
            "thunderbird": "Mozilla Thunderbird.app",
            "grammarly": "Grammarly Desktop.app",
            "loom": "Loom.app",
            "tailscale": "Tailscale.app"
        } # obivously adopted from chatgpt

    if app in names:
        app = names[app]
        subprocess.run(["open", "-a", app])
    result = subprocess.run(
        ["open", "-a", app],
        capture_output=True,
        text=True
    )

    if result.returncode ==0 :
        print(f"Opening {app}...")
        print(f"Opened {app}")
    