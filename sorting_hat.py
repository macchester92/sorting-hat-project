import os
import sys
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

origin_path = sys.argv[1] if len(
    sys.argv) > 1 else '/Users/macchester92/Desktop/Sorting Hat'
dest_path = '/Users/macchester92/Desktop/test_folder'

# define trigger for observer
class SortingHatHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(origin_path):
            print(src_path)

            #resolves error -43 when directory is partially moved to the sorting folder
            if os.path.isdir(file):
                time.sleep(5)

            move_file_to_destination_dir(file)


# actions to apply
def move_file_to_destination_dir(file):
    old_file_path = os.path.join(origin_path, file)
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
observer.schedule(event_handler, origin_path, recursive=True)


observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
