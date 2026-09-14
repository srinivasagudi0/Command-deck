def scan():
    # need to search google a lot and I know all of them now and I memorized them now
    import psutil
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery percentage: \t\t{battery.percent}%")
        if battery.power_plugged:
            print("Battery status: Charging")
        else:
            print("Battery status: Unplugged")
    else:
        print("Something went wrong with battery detection")

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage:
        print("CPU: \t\t{cpu_usage}")

    memory = psutil.virtual_memory()
    if memory:
        print(f"Memory (RAM): \t\t {memory.percent}%")

    disk = psutil.disk_usage('/')

    if disk:
        used_gb = round(disk.used / (1024**3), 2)
        total_gb = round(disk.total / (1024**3), 2)
        left_gb = (total_gb-used_gb)
        free_percent = round(100- disk.percent, 1)

        print(f"Storage: \t\t {left_gb}({free_percent})% available.")

    import platform

    mac_version = platform.mac_ver()[0]
    if mac_version:
        print(f"macOS Version: \t\t {mac_version}")

    import socket
    device_name = socket.gethostbyname()
    if device_name:
        print(f"Device Name: \t\t {device_name}")

    import requests
    is_connected = False
    try:
        requests.get("<unsafe_url>https://www.apple.com</unsafe_url>", timeout=2)
        is_connected = True
    except:
        is_connected = False
    if is_connected:
        print("Network: \t\t Online")
    else:
        print("Network: \t\t Offline")

