from tkinter import *
from tkinter import messagebox

Settings = Tk()


Settings.geometry("310x600")
Settings.title("Settings")
Settings.config(background="Black")

Ändra_Bakgrundsbild = Label(Settings,text="Bakgrundsbild:",font="Arial 12 bold",fg="White",bg="Grey")
Ändra_Bakgrundsbild.place(x=15,y=50)

Settings.mainloop()