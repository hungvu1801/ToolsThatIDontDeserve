import os
import re
import tkinter as tk
from tkinter.filedialog import askdirectory



def get_folder_dir() -> None:
	root = tk.Tk()
	root.withdraw()      
	folder_dir = askdirectory(title="Select Folder")
	return folder_dir

def collect_folder(folder_dir) -> None:
	file_list = os.listdir(folder_dir)
	folder_dictionary = dict()

	for file_name in file_list:
		# file_name_base = os.path.splitext(file_name)[0]
		folder_name = re.match(r'^([A-Z0-9]*_\w{1})', file_name)
		if folder_name:
			folder_name = folder_name.group()
		else: continue
		if folder_name not in folder_dictionary:
			folder_dictionary[folder_name] = list()
		folder_dictionary[folder_name].append(file_name)
	# print(folder_dictionary)
	for folder_name in folder_dictionary.keys():
		os.makedirs(os.path.join(folder_dir, folder_name))
		for file_name in folder_dictionary[folder_name]:
			old_directory = os.path.join(folder_dir, file_name)
			new_directory = os.path.join(folder_dir, folder_name, file_name)
			os.replace(old_directory, new_directory)

def collect_files() -> None:
	try:
		folder_dir = get_folder_dir()
		if not folder_dir:
			return
		collect_folder(folder_dir)
		input("Collect file is successful. Press any key to continue.")
	except Exception as e:
		print(f"Error: {e}.\nCollect file is NOT successful. Press any key to continue.")
