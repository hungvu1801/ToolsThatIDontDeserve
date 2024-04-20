import pandas
import re
import os
import zipfile

def open_folder():
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    folder_name = filedialog.askdirectory(initialdir = ".",title = "Select folder")
    return folder_name

def create_zip_file(zip_folder_name, list_files):
    zip_folder_name += ".zip"
    with zipfile.ZipFile(zip_folder_name, 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        for file_path in list_files:
            file_name = os.path.basename(file_path)
            my_zip.write(filename=file_path, arcname=file_name)

def main():
    folder_name = open_folder()
    if not folder_name:
        return
    file_groups = {}
    list_files = os.listdir(folder_name)
    for file_name in list_files:
        zip_folder_name = re.match('^([A-Z0-9]*)', file_name)
        if zip_folder_name:
            zip_folder_name = zip_folder_name.group()
        else: continue
        if zip_folder_name not in file_groups:
            file_groups[zip_folder_name] = list()
        file_groups[zip_folder_name].append(os.path.join(folder_name, file_name))
    for prefix, list_files in file_groups.items():
        create_zip_file(prefix, list_files)