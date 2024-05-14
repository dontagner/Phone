import time
from tkinter import *
from tkinter import messagebox
import random
from playsound import playsound
import threading

window = Tk()
window.geometry("310x600")
window.title("rizzaphone")
window.config(background="black")

Telefon_färg = Canvas(window, width=275,height=530,bg="pink")
Telefon_färg.place(x=15,y=15)


Laddning = 0
for i in range(Laddning,101):
    Rand = random.randint(1,4)
    if Rand == 1:
        time.sleep(0.1)
    else:
        LaddningVisa = Label(window,text=("Loading",i,"%"))
        LaddningVisa.place(x=110,y=250)
        time.sleep(0.1)
        Laddning = i+1
        LaddningVisa.update()
        LaddningVisa.place_forget()
        
playsound("Slutprojekt/Ljud/Load.mp3")
       
Klart = Label(window,text="Klart")   
def klart():
    Klart.place(x=135,y=250)
    window.after(5000,förstöra)

def förstöra():
    Klart.place_forget()
klart()

window.mainloop()