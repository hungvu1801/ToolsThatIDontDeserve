import re
import os
from pathlib import Path
import zipfile
import tkinter as tk
from tkinter import filedialog
import concurrent.futures


def open_folder() -> None:
    root = tk.Tk()
    root.withdraw()
    folder_name = filedialog.askdirectory(initialdir=".", title="Select folder")
    return folder_name


def create_zip_file(zip_folder_name, list_files) -> None:
    zip_folder_name += ".zip"
    with zipfile.ZipFile(
        zip_folder_name, "w", compression=zipfile.ZIP_DEFLATED
    ) as my_zip:
        for file_path in list_files:
            file_name = os.path.basename(file_path)
            my_zip.write(filename=file_path, arcname=file_name)


def zip_files() -> None:
    try:
        folder_name = open_folder()
        if not folder_name:
            return
        file_groups = {}
        list_files = os.listdir(folder_name)
        for file_name in list_files:
            zip_folder_name = re.match(r"^([A-Z0-9]*_\w{1})", file_name)
            if zip_folder_name:
                zip_folder_name = zip_folder_name.group()
            else:
                continue
            if zip_folder_name not in file_groups:
                file_groups[zip_folder_name] = list()
            file_groups[zip_folder_name].append(os.path.join(folder_name, file_name))
        for prefix, list_files in file_groups.items():
            create_zip_file(prefix, list_files)
        input("Zip files is successful. Press any key to continue.")
    except Exception as e:
        input(f"Error: {e}.\nZip file is NOT successful. Press any key to continue.")


def create_unzip_file(zip_file_name, extract_path) -> None:
    with zipfile.ZipFile(zip_file_name, "r") as my_zip:
        my_zip.extractall(path=extract_path)


def unzip_files() -> None:
    try:
        folder_name = open_folder()

        while not folder_name:
            print("Not a folder. Press select again.")
            folder_name = open_folder()

        folder_name_path = Path(folder_name)
        list_files = os.listdir(folder_name)
        list_zip_files = []
        for file_name in list_files:
            if file_name.endswith(".zip"):
                zip_file_path = folder_name_path.joinpath(file_name)
                zip_file_path_str = zip_file_path.as_posix()

                zip_file_path_without_ext = zip_file_path.stem
                folder_unzip_path = folder_name_path.joinpath(zip_file_path_without_ext)
                folder_unzip_path_str = folder_unzip_path.as_posix()
                list_zip_files.append((zip_file_path_str, folder_unzip_path_str))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(
                    create_unzip_file, zip_file_path_str, folder_unzip_path_str
                )
                for zip_file_path_str, folder_unzip_path_str in list_zip_files
            ]
            for f in futures:
                f.result()

        input("Zip files is successful. Press any key to continue.")
    except Exception as e:
        input(f"Error: {e}.\nZip file is NOT successful. Press any key to continue.")
