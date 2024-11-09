import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import functions
from tkinter import *
from tkinter import dialog
from tkinter import filedialog

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
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()
    slaves = object.pack_slaves()
    for x in slaves:
        x.destroy()

def file_click():
    """Function for selecting a MAPLEAF file"""
    page.filename = filedialog.askopenfilename(title="Select A .MAPLEAF File", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    Label(page, text=f'File chosen: {page.filename}', foreground='red').grid(row=2, column=0)

def motor_page():
    """Motor definition page"""
    clear(page)
    Label(page, text="BRRRRR").grid(row=1, column=0)
 
def rocket_page():
    """Rocket definition page"""
    clear(page)
    Checkbutton(page, text="Does rocket exist?").grid(row=1, column=0)
    Label(page, text="Rocket stuff...").grid(row=2, column=0)
    #create file selection button
    Button(page, text='Choose data file', width=14, command=file_click, activeforeground='red', background='black', foreground='white').grid(row=4, column=0)
    
    # define plot for rocket display
    fig, ax = plt.subplots()
    x = [1,2,3,4]
    y = [1,4,9,16]

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