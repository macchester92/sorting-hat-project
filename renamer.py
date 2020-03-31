import os

os.chdir('/Users/macchester92/Desktop/source')


for file in os.listdir():
	file_name, file_ext = os.path.splitext(file)
	new_name = f'{file_name}01{file_ext}'
	os.rename(file, new_name)
