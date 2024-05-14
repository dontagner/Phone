from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import time

flappy = Tk()
flappy.geometry('1000x600')
flappy.title('Flappy bird')


x = 150
y = 300
poäng = 0
fart = 10
game_over = False

bild_fågel = Image.open('Slutprojekt/Bilder/fagel.png')
bild_fågel = ImageTk.PhotoImage(bild_fågel)

bild_rör_nere = Image.open('Slutprojekt/Bilder/ror.png')
bild_rör_uppe = bild_rör_nere.rotate(180)

bild_rör_nere = ImageTk.PhotoImage(bild_rör_nere)
bild_rör_uppe = ImageTk.PhotoImage(bild_rör_uppe)

bild_starta_om = Image.open('Slutprojekt/Bilder/starta_om.png')
bild_starta_om = ImageTk.PhotoImage(bild_starta_om)


canvasflappy = Canvas(flappy, highlightthickness=0, bg= '#00bfff')
canvasflappy.place(relheight= 1, relwidth= 1)

text_poäng = canvasflappy.create_text(50,50, text= '0', fill = 'white', font =('D3 Egoistism outline',30))

fågel = canvasflappy.create_image(x,y, anchor= 'nw', image = bild_fågel)
rör_uppe = canvasflappy.create_image(1200, -550, anchor= 'nw', image = bild_rör_uppe)
rör_nere = canvasflappy.create_image(1200, 550, anchor= 'nw', image = bild_rör_nere)

def rör_fågel_knapp(event):
    global x,y
    if not game_over:
        y -=30
        canvasflappy.coords(fågel ,x,y)

flappy.bind( "<space>", rör_fågel_knapp)

def flytta_fågel():
    global x, y
    y += 5
    canvasflappy.coords(fågel, x, y)
    if y < 0 or y > canvasflappy.winfo_height():
        spel_över()
    
    if not game_over:
        flappy.after(50, flytta_fågel)

def flytta_rör():
    global poäng,game_over,fart
    canvasflappy.move(rör_uppe, -fart, 0)
    canvasflappy.move(rör_nere, -fart, 0)
    if canvasflappy.coords(rör_nere)[0] < -100:
        h = flappy.winfo_height()
        num = random.choice([i for i in range(160,h,160)])
        canvasflappy.coords(rör_nere, flappy.winfo_width(), num + 160)
        canvasflappy.coords(rör_uppe, flappy.winfo_width(), num - 900)

    if 145 < canvasflappy.coords(rör_nere)[0] <155:
        poäng += 1
        fart += 1
        canvasflappy.itemconfigure(text_poäng, text= str(poäng))

    if canvasflappy.coords(rör_nere):
        if (canvasflappy.bbox(fågel)[0] < canvasflappy.bbox(rör_nere)[2] and 
    canvasflappy.bbox(fågel)[2] > canvasflappy.bbox(rör_nere)[0] and 
    (canvasflappy.bbox(fågel)[1] < canvasflappy.bbox(rör_uppe)[3] or 
    canvasflappy.bbox(fågel)[3] > canvasflappy.bbox(rör_nere)[1])):
                spel_över()
    if not game_over:
        flappy.after(50, flytta_rör)





def starta_om_spel():
    global x,y,poäng,fart,game_over
    x = 150
    y = 300
    poäng = 0
    fart = 10
    game_over = False
    canvasflappy.coords(fågel, x,y)
    canvasflappy.coords(rör_uppe, 1200, -550)
    canvasflappy.coords(rör_nere, 1200, 550)
    canvasflappy.itemconfigure(text_poäng, text="0")
    text_game_over.place_forget()
    starta_om_knapp.place_forget()
    flytta_fågel()
    flytta_rör()


    

def spel_över():
    global game_over
    game_over = True
    text_game_over.place(relx= 0.5, rely=0.4, anchor='center')
    starta_om_knapp.place(relx=0.5, rely= 0.7, anchor= 'center')


text_game_over = Label(flappy, text= 'Du suger! spela igen?', font=('D3 Egoistism outline',30),fg='White', bg='#00bfff')
starta_om_knapp = Button(flappy, border=0, image= bild_starta_om, activebackground='#00bfff', bg= '#00bfff', command= starta_om_spel)


flappy.after(50, flytta_fågel)
flappy.after(50, flytta_rör)


flappy.mainloop()