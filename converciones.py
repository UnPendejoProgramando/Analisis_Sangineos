from tkinter import *
from base import Base

class Glucosa(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.valorObtenido = DoubleVar()
    def convertir(self):
        self.resultado = self.valorObtenido.get() * 18.02
        Label(self.second, text = "Glucosa " + str(self.resultado) + " mg/dL", font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 100)

class Acido(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.valorObtenido = DoubleVar()
    def convertir(self):
        self.resultado = self.valorObtenido.get() * 0.02
        Label(self.second, text = "Acido úrico " + str(self.resultado) + " mg/dL", font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 100)

class Colesterol(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.valorObtenido = DoubleVar()
    def convertir(self):
        self.resultado = self.valorObtenido.get() * 380.66
        Label(self.second, text = "Colesterol " + str(self.resultado) + " mg/dL", font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 100)

class Urea(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.valorObtenido = DoubleVar()
    def convertir(self):
        self.resultado = self.valorObtenido.get() * 6.01
        Label(self.second, text = "Urea " + str(self.resultado) + " mg/dL", font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 100)

class Trigliceridos(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.valorObtenido = DoubleVar()
    def convertir(self):
        self.resultado = self.valorObtenido.get() * 87.5
        Label(self.second, text = "Trigliceridos " + str(self.resultado) + " mg/dL", font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 100)

class Creatinina(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.valorObtenido = DoubleVar()
    def convertir(self):
        self.resultado = self.valorObtenido.get() * 0.01
        Label(self.second, text = "Creatinina " + str(self.resultado) + " mg/dL", font = ("Arial", 12), bg = "#F3E5F5").place(x = 50, y = 100)