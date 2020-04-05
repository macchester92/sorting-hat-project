import os
import sys


dest_path = '/Users/macchester92/Desktop/test_folder'

# for root, dirs, files in os.walk(dest_path, topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

print(os.path.getsize('/Users/macchester92/Desktop/test_folder/channel'))