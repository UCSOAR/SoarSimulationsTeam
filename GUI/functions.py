from tkinter import *
from tkinter import dialog
from tkinter import filedialog
import os
import sys
import subprocess

#function to define resource path for image taken from reference [4]
def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#Define function for file selection
def fileClick(window):
    window.filename = filedialog.askopenfilename(title="Select A File", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    Label (window, text=f'File chosen: {window.filename}', foreground='red').grid(column=1,row=12)

def run():
    subprocess.run("conda run -n SOAR MAPLEAF C:\\Users\\zackg\\Documents\\Coding\\MAPLEAF-master\\MAPLEAF\\Examples\\Simulations\\Zack2.mapleaf --silent", shell=True)