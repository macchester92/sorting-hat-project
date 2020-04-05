import os
import sys
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from renamer import FileHandler
import logging

sorter_path = sys.argv[1] if len(
    sys.argv) > 1 else '/Users/macchester92/Desktop/Sorting Hat'
dest_path = sys.argv[2] if len(
    sys.argv) > 1 else'/Users/macchester92/Desktop/test_folder'



class SortingHatHandler(FileSystemEventHandler):
    def on_created(self, event):
        for obj in os.listdir(sorter_path):
            if not obj.startswith('.') or not obj.endswith('.app'):
                # file = both file and directory
                file = FileHandler(obj)
                if file.is_ready():
                    file.move()


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
