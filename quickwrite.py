import os
import sys
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from renamer import File

sorter_path = sys.argv[1] if len(
    sys.argv) > 1 else '/Users/macchester92/Desktop/Sorting Hat'
dest_path = '/Users/macchester92/Desktop/test_folder'



class SortingHatHandler(FileSystemEventHandler):
    def on_created(self, event):
        for obj in os.listdir(sorter_path):
            if not obj.startswith('.'):
                # file = both file and directory
                file = File(obj)
                pAAASSS = file.filepath
                verify(pAAASSS)
                if verify(file.filepath):
                    file.move()
                else:
                    print('Not Verified')


def verify(pAAASSS):
    verification = False
    if os.path.isdir(pAAASSS):
        print('Directory deteced')
        time.sleep(2)
        sort_size = -1
        while sort_size != dir_size(pAAASSS):
            sort_size = dir_size(pAAASSS)
            print(sort_size)
            time.sleep(1)
        verification = True
    if os.path.isfile(pAAASSS):
        print('File detected')
        file_size = -1
        while file_size != os.path.getsize(pAAASSS):
            file_size = os.path.getsize(pAAASSS)
            print(file_size)
            time.sleep(0.5)
        verification = True
    return verification  

def dir_size(file_path):
    total_size = 0 
    for root, dirs, files in os.walk(file_path):
        for file in files:
            parsing_path = os.path.join(root, file)
            total_size += os.path.getsize(parsing_path)
    return total_size

# configuring the app
observer = Observer()
event_handler = SortingHatHandler()
observer.schedule(event_handler, sorter_path, recursive=True)


observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
