from tkinter import *

class Base:
    def __init__(self):
        self.titulo = "Conversor"
    def mostrar(self):
        self.valorObtenido = DoubleVar()
        self.second = Toplevel()
        self.second.title(self.titulo)
        self.second.geometry("400x250")
        self.second.iconbitmap("icono/icono.ico")
        self.second.config(bg = "#E1BEE7")
        self.second.resizable(0,0)
        Label(self.second, text = "Convercion de " + self.titulo, font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 0)
        Label(self.second, text = self.titulo, font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 50)
        Entry(self.second, textvariable = self.valorObtenido).place(x = 150, y = 50)
        Label(self.second, text = "mmol/L", font = ("Arial", 12), bg = "#F3E5F5").place(x = 250, y = 50)
        self.connvertir = Button(self.second, text = "Convertir", width = 10, height = 2, font = ("Arial", 12), bg = "#F3E5F5", command = self.convertir).place(x = 50, y = 150)
        self.salir = Button(self.second, text = "Salir", width = 10, height = 2, font = ("Arial", 12), bg = "#F3E5F5", command = self.destruir).place(x = 150, y = 150)
    def destruir(self):
        self.second.destroy()