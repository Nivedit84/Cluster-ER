import os
import datetime
from utils.kubectl import run_kubectl
import shutil


def capture_incident():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder_name = f"incident_{timestamp}"

    os.makedirs(folder_name, exist_ok=True)

    with open(f"{folder_name}/all_resources.txt", "w") as f:
        f.write(run_kubectl("get all -A"))
        
    
    with open(f"{folder_name}/events.txt", "w") as f:
        f.write(run_kubectl("get events -A"))
    
    print(f"Captured incident data in folder: {folder_name}")
    archive_name = shutil.make_archive(folder_name, 'gztar', folder_name)
    print(f" Compress incident data: {archive_name}")