import psutil
import datetime
import datetime
import platform
import socket
import requests
import os

def scan():
    # need to search google a lot and I know all of them now and I memorized them now

    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery percentage: \t\t{battery.percent}%")
        if battery.power_plugged:
            print("Battery status: \t\t Charging")
            print("Estimated Time Remaining: \t\t Unlimited(plugged in)")
        else:
            print("Battery status: Unplugged")
            print(f"Estimated Time Remaining: \t\t {str(datetime.timedelta(seconds=battery.secsleft))}")
    else:
        print("Something went wrong with battery detection")

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage:
        print("CPU: \t\t{cpu_usage}")

    memory = psutil.virtual_memory()
    if memory:
        print(f"Memory (RAM): \t\t {memory.percent}%")

    consuming_apps = [p.info for p in psutil.process_iter(['name', 'memory_info'])] # Gives me th ellsit of processes happenign
    top_app = max(consuming_apps, key=lambda p:p['memory_info'].rss if p["memory_info"] else 0)
    mb_used = top_app['memory_info'].rss / (1024* 1024)
    print(f"Top App: \t\t {top_app['name']} ({mb_used:.2f}) MB")
 
    disk = psutil.disk_usage('/')

    if disk:
        used_gb = round(disk.used / (1024**3), 2)
        total_gb = round(disk.total / (1024**3), 2)
        left_gb = (total_gb-used_gb)
        free_percent = round(100- disk.percent, 1)

        print(f"Storage: \t\t {left_gb}({free_percent})% available.")

    trash_size = 0
    trash_path = os.path.expanduser("~/.Trash")

    if os.path.exists(trash_path):
        for dir_path, dirnames, filenames in os.walk(trash_path):
            for f in filenames:
                fp = os.path.join(dir_path,f)
            if not os.path.islink(fp):
                trash_size += os.path.getsize(fp)
        print(f"Trash size: {trash_size / (1024**3):.2f} GB")


    chip_info = platform.processor()
    machine_type = platform.machine()

    if chip_info and machine_type:
        print(f"Processor: \t\t {chip_info}")
        print(f"Architecture: {machine_type}")

    core_count = os.cpu_count()
    if core_count:
        print(f"Total CPU Cores: \t\t {core_count}")

    mac_version = platform.mac_ver()[0]
    if mac_version:
        print(f"macOS Version: \t\t {mac_version}")

    
    device_name = socket.gethostbyname()
    if device_name:
        print(f"Device Name: \t\t {device_name}")

    
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

