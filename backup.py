import os
import shutil
import datetime
import schedule
import time

source_dir = "/Users/appacademystudent/Downloads"
destination_dir = "/Users/appacademystudent/Desktop/Backup_Folder"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Download copied to: {dest_dir}")
    except FileExistsError:
        print(f"Download already exists in: {dest}")
        
schedule.every().week.at("20:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir)) 

while True:
    schedule.run_pending()
    time.sleep(60) #If I restart the computer, just re-run the file
    