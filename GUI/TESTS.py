from tkinter import *
import matplotlib.pyplot as plt
import functions
import pages

#initialize GUI window
window = Tk()

#title the window
window.title('MAPLEAF')

#take and display SOAR.png photo from computer
photo_directory = functions.img_resource_path("img/Logo.png")
logo = PhotoImage(file=photo_directory)
logo_label = Label(window, image=logo)
logo_label.grid(column=1, row=1)

#window size
window.geometry('800x600')

#button to run MAPLEAF
Button (window, text='Run Simulation', width=12, command=functions.run, activebackground='red', foreground='red',).grid(column=2, row=13)
Button (window, text='Motor', width=12, command=pages.page1(window), activebackground='red', foreground='red',).grid(column=2, row=15)

#run window loop
window.mainloop()