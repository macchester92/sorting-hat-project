import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = sys.argv[1] if len(sys.argv) > 1 else '/Users/macchester92/Desktop/Sorting Hat'
dest = '/Users/macchester92/Desktop/test_folder'

# define trigger for observer
class SortingHatHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(path):
            move_file_to_destination_dir(file)


# actions to apply
def move_file_to_destination_dir(file):
    src_path = f'{path}/{file}'
    dest_path = f'{dest}/{file}'
    return os.rename(src_path, dest_path)





observer = Observer()
event_handler = SortingHatHandler()
observer.schedule(event_handler, path, recursive=True)


observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
