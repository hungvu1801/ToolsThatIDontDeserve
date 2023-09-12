import tkinter as tk
from tkinter import Tk, Label, Button
from tkinter import filedialog

import pandas as pd
import os
import re
import logging
from datetime import datetime
logging.basicConfig(
	filename="mainlog.log",
	level=logging.INFO, 
	format="%(asctime)s: %(levelname)s : %(message)s ")

def mkdir():
  try:
    os.mkdir("Tmp")
    logging.info("Created folder Tmp")
  except FileExistsError:
    logging.info("Folder Tmp Existed.")
    pass

def getUserDirectory():
  # get a directory path by user
  currDir = os.getcwd()
  filepath=filedialog.askdirectory(
    initialdir=currDir,
    title="Choose image folder")
  return filepath
  
def processFiles(filepath):

  fileName = datetime.now().strftime("%Y%m%d_%H%m")
  filesList = os.listdir(filepath)
  uniqueName = set()
  for file in filesList:
    filename, _ = os.path.splitext(file)
    filename = filename.split("_")[1:-1]

    filename = " ".join(filename)
    uniqueName.add(filename)
  
  logging.info(f"Writing file {fileName}.csv")
  with open(f"./Tmp/{fileName}.csv", "w") as wf:
    wf.write("Names\n")
    for name in uniqueName:
      wf.write(f"{name}\n")

def main():
  mkdir()

  filepath = getUserDirectory()
  if filepath:
    logging.info(filepath)
  else:
    return

  processFiles(filepath)
