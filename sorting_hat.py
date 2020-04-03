import os
import sys
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sorter_path = sys.argv[1] if len(
    sys.argv) > 1 else '/Users/macchester92/Desktop/Sorting Hat'
dest_path = '/Users/macchester92/Desktop/test_folder'


class SortingHatHandler(FileSystemEventHandler):
    def on_created(self, event):
        for file in os.listdir(sorter_path):
            if not file.startswith('.'):
                # file = both file and directory
                file_path = os.path.join(sorter_path, file)
                if os.path.isdir(file_path):
                    print('Directory deteced')
                    sort_size = -1
                    while sort_size != dir_size(file_path):
                        sort_size = dir_size(file_path)
                        time.sleep(2)
                if os.path.isfile(file_path):
                    print('File detected')
                    file_size = -1
                    while file_size != os.path.getsize(file_path):
                        file_size = os.path.getsize(file_path)
                        time.sleep(0.5)
                print('Moving...')
                move_file_to_destination_dir(file)

# To get size of current directory
def dir_size(file_path):
    total_size = 0 
    for root, dirs, files in os.walk(file_path):
        for file in files:
            parsing_path = os.path.join(root, file)
            total_size += os.path.getsize(parsing_path)
    return total_size
# actions to apply


def move_file_to_destination_dir(file):
    old_file_path = os.path.join(sorter_path, file)
    if not file.startswith('.'):
        file_name, file_ext = os.path.splitext(file)
        result = check_folder(file_ext, file)
        return shutil.move(old_file_path, result)


def check_folder(file_ext, file):
    new_file_path = os.path.join(dest_path, file_ext[1:])
    if not os.path.exists(new_file_path):
        os.mkdir(new_file_path)
    mega_path = os.path.join(new_file_path, file)
    if not mega_path:
        os.mkdir(mega_path)
    return mega_path


# configuring the app
observer = Observer()
event_handler = SortingHatHandler()
observer.schedule(event_handler, sorter_path, recursive=True)


observer.start()
try:
    while True:
        time.sleep(3)
except KeyboardInterrupt:
    observer.stop()
observer.join()
