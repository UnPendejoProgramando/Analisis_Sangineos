#-*-coding:utf-8-*-
try:
    from Tkinter import *
except:
    from tkinter import *

from qs3 import Qs3
from qs6 import Qs6

def salir():
    screen.destroy()


screen = Tk()
screen.title("Laboratorio de Analisis Clinicos DM")
screen.geometry("400x150")
screen.resizable(0,0)
screen.iconbitmap("icono/icono.ico")
screen.config(bg = "#D1C4E9")

Label(screen, text = "Laboratorio de Analisis Clinicos DM", font = ("Arial", 14), bg = "#EDE7F6").place(x = 50, y = 0)

opcion1 = Qs3()
opcion2 = Qs6()

qs3 = Button(screen, text = "QS3", font = ("Arial", 12), bg = "#EDE7F6", width = 8, height = 2, command = opcion1.obtener)
qs3.place(x = 60, y = 50)

qs6 = Button(screen, text = "QS6", font = ("Arial", 12), bg = "#EDE7F6", width = 8, height = 2, command = opcion2.obtener)
qs6.place(x = 160, y = 50)

salir = Button(screen, text = "Salir", font = ("Arial", 12), bg = "#EDE7F6", width = 8, height = 2, command = salir)
salir.place(x = 260, y = 50)

screen.mainloop()
