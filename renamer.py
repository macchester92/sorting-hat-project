import os
import sys
import shutil
import time


sorter_path = sys.argv[1] if len(
    sys.argv) > 1 else '/Users/macchester92/Desktop/Sorting Hat'
dest_path = sys.argv[2] if len(
    sys.argv) > 1 else'/Users/macchester92/Desktop/test_folder'

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    @property
    def filepath(self):
        return os.path.join(sorter_path, self.filename)

    @property
    def new_filepath(self):
        _, file_ext = os.path.splitext(self.filename)
        temp_path = os.path.join(dest_path, file_ext[1:])
        if not os.path.exists(temp_path):
            os.mkdir(temp_path)
        new_filepath = os.path.join(temp_path, self.filename)
        if not new_filepath:
            os.mkdir(new_filepath)
        return new_filepath

    @property
    def dir_size(self):
        total_size = 0
        for root, dirs, files in os.walk(self.filepath):
            for file in files:
                parsing_path = os.path.join(root, file)
                total_size += os.path.getsize(parsing_path)
        return total_size

    
    def is_ready(self):
        ''' Checks if the file is ready to be moved to destination folder. Note: for large
        directories time.sleep(2) is set to avoid miscalculations in direcotry size, leading
        to error -43
        '''
        if os.path.isdir(self.filepath):
            time.sleep(2)
            sort_size = -1
            while sort_size != self.dir_size:
                sort_size = self.dir_size
                time.sleep(1)
        if os.path.isfile(self.filepath):
            file_size = -1
            while file_size != os.path.getsize(self.filepath):
                file_size = os.path.getsize(self.filepath)
                time.sleep(0.5)
        return True

    def move(self):
        return shutil.move(self.filepath, self.new_filepath)
