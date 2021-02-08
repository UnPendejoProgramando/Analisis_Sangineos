from tkinter import *
from converciones import *
from menu import *


class Qs3:
    def obtener(self):
        self.screenTwo = Toplevel()
        self.screenTwo.geometry("400x350")
        self.screenTwo.title("QS3")
        self.screenTwo.config(bg = "#D1C4E9")
        self.screenTwo.iconbitmap("icono/icono.ico")
        self.screenTwo.resizable(0,0)
        Label(self.screenTwo, text = "Quimica Sanguinea 3", bg = "#EDE7F6", font = ("Arial", 12)).place(x = 100, y = 0)
        #---------Instancias-----
        self.glucosaa = Glucosa("Glucosa")
        self.acidoo = Acido("Ácido úrico")
        self.coleste = Colesterol("Colesterol")
        #---------Opciones--------
        self.glucosa = Button(self.screenTwo, text = "Glocosa", font = ("Arial", 12), bg = "#EDE7F6", width = 10, height = 2, command = self.glucosaa.mostrar).place(y = 30, x = 50)
        self.acido = Button(self.screenTwo, text = "Acido urico", font = ("Arial", 12), bg = "#EDE7F6", width = 10, height = 2, command = self.acidoo.mostrar).place(y = 110, x = 50)
        self.colesterol = Button(self.screenTwo, text = "Colesteron", font = ("Arial", 12), bg = "#EDE7F6", width = 10, height = 2, command = self.coleste.mostrar).place(y = 190, x = 50)
        self.salir = Button(self.screenTwo, text = "Salir", font = ("Arial", 12), bg = "#EDE7F6", width = 10, height = 2, command = self.cerrar_ventana).place(y = 270, x = 50)
    def cerrar_ventana(self):
        self.screenTwo.destroy()