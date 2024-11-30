import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import functions
from tkinter import *
from tkinter import dialog
from tkinter import filedialog
import pandas as pd
from motor_functions import convert_static_fire_data_to_MAPLEAF_file

# create tkinter window
window = Tk()
window.title("MAPLEAF")

# change tkinter icon
window.iconphoto(False, PhotoImage(file='img/Logo.png'))

# create menu frame
menu = Frame(window)
menu.pack(fill=Y)

# create page frame
page = Frame(master=window, height=800)
page.pack(fill=X)

# show MAPLEAF logo
photo_directory = functions.img_resource_path("img/Logo.png")
logo = PhotoImage(file=photo_directory)
logo_label = Label(page, image=logo)
#welcome_message = Label(page, text="Welcome to MAPLEAF").grid(column=1, row=2)
logo_label.pack()

page.pack(fill=X)

# clear screen function
def clear(object):
    # destroy grid objects
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()
        # destroy pack objects
    slaves = object.pack_slaves()
    for x in slaves:
        x.destroy()

# function for selecting a motor file
def file_click_motor():
    """Function for selecting a MAPLEAF file"""
    page.motorFilename = filedialog.askopenfilename(title="Select a MAPLEAF Motor File", filetypes=(("Motor Files", "*.txt"), ("CSV Files", "*.csv"), ("All Files", "*.*")))
    motor_page()

# function for selecting a MAPLEAF rocket file
def file_click_rocket():
    """Function for selecting a MAPLEAF file"""
    page.rocketFilename = filedialog.askopenfilename(title="Select A .MAPLEAF File", filetypes=(("MAPLEAF Files", "*.MAPLEAF"), ("All Files", "*.*")))
    clear(page)
    rocket_page()

# motor set up page
def motor_page():
    """Motor definition page"""
    clear(page)
    Label(page, text="BRRRRR").grid(row=1, column=0)
    # create file selection button
    Button(page, text='Choose data file', width=14, command=file_click_motor, activeforeground='red', background='black', foreground='white').grid(row=8, column=0)

    try: 
        # show file chosen
        #Label(page, text=f'File Chosen: {page.motorFilename}', foreground='red').grid(row=7, column=3)

        # output file inputs
        Label(page, text="Output File Name").grid(row=1, column=0)
        output_file_name = Entry(page, width=10).grid(row=1, column=1)
        Label(page, text=".txt").grid(row=1, column=2)

        # write toggle
        write = Checkbutton(page, text="Write to Output File").grid(row=2, column=0)

        # extend toggle
        extend = Checkbutton(page, text="Extend Burn time").grid(row=3, column=0)

        # Burn time extension inputs
        Label(page, text="Burn Time Extension").grid(row=4, column=0)
        extension = Entry(page, width=10).grid(row=4, column=1)
        Label(page, text="seconds").grid(row=4, column=2)

        # estimation toggle
        estimation = Checkbutton(page, text="Estimate Average Thrust").grid(row=5, column=0)

        # estimation inputs
        Label(page, text="Estimation Thrust").grid(row=6, column=0)
        estimation_avg_thrust = Entry(page, width=10).grid(row=6, column=1)
        Label(page, text="Newtons").grid(row=6, column=2)

        # run mapleaf motor file generator
        #convert_static_fire_data_to_MAPLEAF_file(page.motorFilename, output_file_name.get(), extend.get(), extension.get(), estimation.get(), estimation_avg_thrust.get())
    except:
        Label(page, text="Upload Static Fire Data or MAPLEAF Motor File").grid(row=2, column=0)
        # define plot for rocket display
        fig, ax = plt.subplots()
        x = []
        y = []

        plt.plot(x, y)

        canvas = FigureCanvasTkAgg(fig, page)
        canvas.get_tk_widget().grid(row=3, column=0)
 
def rocket_page():
    """Rocket definition page"""
    clear(page)
    Checkbutton(page, text="Does rocket exist?").grid(row=1, column=0)
    Label(page, text="Rocket stuff...").grid(row=2, column=0)
    #create file selection button
    Button(page, text='Choose data file', width=14, command=file_click_rocket, activeforeground='red', background='black', foreground='white').grid(row=4, column=0)
    Label(page, text=f'File chosen: {page.rocketFilename}', foreground='red').grid(row=5, column=0)
    
    # define plot for rocket display
    fig, ax = plt.subplots()
    x = []
    y = []

    plt.plot(x, y)

    canvas = FigureCanvasTkAgg(fig, page)
    canvas.get_tk_widget().grid(row=3, column=0)

def help_page():
    """Help page"""
    clear(page)
    Label(page, text="Wish I could help... StackOverFlow??").pack()


# persistent menu buttons
motor_button = Button(menu, text="Motor", command=motor_page).grid(row=0, column=0)
rocket_button2 = Button(menu, text="Rocket", command=rocket_page).grid(row=0, column=1)
help_button = Button (menu, text="Help", command=help_page).grid(row=0, column=2)

mainloop()