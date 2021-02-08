from tkinter import *
from converciones import *
class Qs6():
    def obtener(self):
        self.screenTree = Toplevel()
        self.screenTree.geometry("400x350")
        self.screenTree.title("QS6")
        self.screenTree.config(bg = "#D1C4E9")
        self.screenTree.iconbitmap("icono/icono.ico")
        self.screenTree.resizable(0,0)
        Label(self.screenTree, text = "Quimica Sanguinea 6", bg = "#EDE7F6", font = ("Arial", 12)).place(x = 100, y = 0)
        #--------Instancias-------
        self.glucosaa = Glucosa("Glucosa")
        self.acidoo = Acido("Ácido úrico")
        self.coleste = Colesterol("Colesterol")
        self.ureaa = Urea("Urea")
        self.trigli = Trigliceridos("Trigliceridos")
        self.creati = Creatinina("Creatinina")
        #---------Opciones--------
        self.glucosa = Button(self.screenTree, text = "Glocosa", bg = "#EDE7F6", font = ("Arial", 12), width = 10, height = 2, command = self.glucosaa.mostrar).place(y = 30, x = 70)
        self.acido = Button(self.screenTree, text = "Acido urico", bg = "#EDE7F6", font = ("Arial", 12), width = 10, height = 2, command = self.acidoo.mostrar).place(y = 110, x = 70)
        self.colesterol = Button(self.screenTree, text = "Colesteron", bg = "#EDE7F6", font = ("Arial", 12), width = 10, height = 2, command = self.coleste.mostrar).place(y = 190, x = 70)
        self.salir = Button(self.screenTree, text = "Salir", bg = "#EDE7F6", font = ("Arial", 12), width = 10, height = 2, command = self.cerrar_ventana).place(y = 270, x = 70)

        self.urea = Button(self.screenTree, text = "Urea", bg = "#EDE7F6", font = ("Arial", 12), width = 10, height = 2, command = self.ureaa.mostrar).place(y = 30, x = 220)
        self.trigliceridos = Button(self.screenTree, text = "Trigliceridos", bg = "#EDE7F6", font = ("Arial", 12), width = 10, height = 2, command = self.trigli.mostrar).place(y = 110, x = 220)
        self.creatinina = Button(self.screenTree, text = "Creatinina", bg = "#EDE7F6", font = ("Arial", 12), width = 10, height = 2, command = self.creati.mostrar).place(y = 190, x = 220)
        
    def cerrar_ventana(self):
        self.screenTree.destroy()
