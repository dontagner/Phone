from tkinter import *
from time import strftime
from PIL import Image, ImageTk
import random

window = Tk()
window.geometry("310x600")
window.title("RazzleDazzle TeleRizz")
window.config(background="black")

def time():
    string = strftime("%H:%M")
    Tiden_Mobil.config(text=string)
    Tiden_Mobil.after(1000, time)
    
Talet = random.randint(1,100)

class GissaTalet(Toplevel):
    def __init__(self, window = None,):
        super().__init__(master= window)       
        self.geometry("600x500")
        self.title("Gissa talet!")
        self.config(background="Black")

        Gissa_Text = Label(self, text="Gissa på ett tal (1-100):", bg="Orange")
        Gissa_Text.place(x=30, y=110)
        Skriv_tal = Entry(self, bg="White")
        Skriv_tal.place(x=200,y=110, width=60)
        

        Välkommen = Label(self, font="Arial", text= "Välkommen till Gissa talet!", bg="Orange")
        Välkommen.place(x=30, y=40)

        def högre_lägre():
            try:
                CoolaTal = int(Skriv_tal.get())
            except:
                Ingen_Siffra = Label(self,bg="Orange", text= "Skriv en siffra mellan 1-100")
                Ingen_Siffra.place(x=30, y=200)
            if CoolaTal < Talet:
                Högre_Tal = Label(self,bg="Orange", text= "Du gissade på Talet: " + str(CoolaTal) + " Talet är Fel.")
                Högre_Tal.place(x=30, y=200)
                Högre_Tal_Sa = Label(self,bg="Orange", text= "Talet är Högre")
                Högre_Tal_Sa.place(x=30, y=220)
            elif CoolaTal > 100:
                Fel_Inmattning = Label(self,bg="Orange", text="Skriv en siffra mellan 1-100")
                Fel_Inmattning.place(x=30, y=200)
            elif CoolaTal > Talet:
                Lägre_Tal = Label(self,bg="Orange", text= "Du gissade på Talet: " + str(CoolaTal) + " Talet är Fel.")
                Lägre_Tal_Sa = Label(self,bg="Orange", text= "Talet är Lägre")
                Lägre_Tal_Sa.place(x=30, y=220)
                Lägre_Tal.place(x=30, y=200)
            elif CoolaTal == Talet:
                Korrekt_Tal = Label(self,bg="Orange", text= "Du gissade på Talet: " + str(CoolaTal) + " Talet är Korrekt!")
                Korrekt_Tal.place(x=30, y=200)
                Korrekt_Tal_Sa = Label(self,bg="Orange", text= "Talet är varken högre eller lägre!")
                Korrekt_Tal_Sa.place(x=30, y=220)
        Gissa_Knapp = Button(self,text="Gissa!",command=högre_lägre, bg="White")
        Gissa_Knapp.place(x=200,y=135, width=60,)

class Miniräknare(Toplevel):
    def __init__(root, window = None,):
        super().__init__(master= window)   
        

        

Telefon_färg = Canvas(window, width=275,height=530,bg="green")
Telefon_färg.place(x=15,y=25)

image = Image.open("wolf.png")
photo = ImageTk.PhotoImage(image)
wolf = Label(window, image=photo, width=250,height=450)
wolf.place(x=25,y=50)


Sättpå_Knapp = Canvas(window, width=30, height=30, bg="Black")
Sättpå_Knapp.place(x=135,y=515)

Kamera = Canvas(window, width=10, height=10, bg="Black")
Kamera.pack(anchor="center",pady=32)


Black_Bar_Topp = Label(window,bg="black",width=35,height=1)
Black_Bar_Topp.place(x=25,y=50)
Black_Bar_Höger = Label(window,bg="black",width=1,height=30)
Black_Bar_Höger.place(x=270,y=50)
Black_Bar_Vänster = Label(window,bg="black",width=1,height=30)
Black_Bar_Vänster.place(x=25,y=50)
Black_Bar_Botten = Label(window,bg="black",width=36,height=1)
Black_Bar_Botten.place(x=25,y=490)


Tiden_Mobil = Label(window,bg="Black",fg="White",font=("Arial 9 bold"))
Tiden_Mobil.place(x=136,y=50)
Fredag = Label(window,text="Fre",bg="Black",fg="White",font=("Arial 9 bold"))
Fredag.place(x=70,y=50)
Batteri = Label(window,text="57%",bg="Black",fg="White",font=("Arial 9 bold"))
Batteri.place(x=220,y=50)



KnappGissa = Button(window, height=2,width=4,text="Gissa",)
KnappGissa.bind("<Button>", lambda e: GissaTalet(window))
KnappGissa.place(x=215,y=350)

KnappMini = Button(window, height=2,width=4,text="Kalk",)
KnappMini.bind("<Button>", lambda e: Miniräknare(window))
KnappMini.place(x=135, y=350)

KnappFunny = Button(window, height=2,width=4,text="bon bon",)
KnappFunny.bind("<Button>", lambda e: Miniräknare(window))
KnappFunny.place(x=55, y=350)


time()
window.mainloop()


