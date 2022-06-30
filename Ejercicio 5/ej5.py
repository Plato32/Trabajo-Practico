# Ejercicio 5
# Usar la narrativa del Ejercicio Nº 1

# Se han agregado nuevos requerimientos al sistema, 
# y usted como programador, debe darles solución:

# La nutricionista cuenta con un archivo llamado “pacientes.json” 
# donde tiene almacenados los datos de cada paciente que atiende. 
# De cada paciente se almacena: nombre, apellido, teléfono, altura(cm) y peso(kg). 

# Se necesita que la aplicación muestre los datos almacenados 
# de los pacientes junto con el IMC y la composición corporal resultantes.
#  Además, se debe permitir modificar los datos del paciente, 
# lo que implica que se actualice tanto el IMC como la composición corporal.

# Para facilitar el desarrollo, 
# la nutricionista le proporciona la estructura que debería tener el sistema 
# y le solicita que se encargue del diseño del mismo.

# Nota: todos los datos del paciente son obligatorios.
import tkinter as tk
from tkinter import BOTTOM, messagebox
from turtle import width
from json import json

class IMC:
    __altura: float
    __peso: float
    __imc: float
    __tipo: str
    def __init__(self ):
        self.master = tk()
        self.master.title("idice de masa corporal")
        self.master.geometry("500x400")
        self.master.resizable(False, False)
        self.master.background = 'beige'
        self.crear_widgets()

        self.titulo = tk.Label(self.master, text="Calculadora de IMC", font=("Helvetica", 16), bg='#f0f0f0')
        self.titulo.pack(side=tk.TOP, fill=tk.X)
        self.epeso = tk.Label(self.master, text="Peso (kg):", font=("Helvetica", 12), bg='#f0f0f0')
        self.epeso.pack(pady=5)
        self.__peso = tk.Entry(self.master, width=20, font=("Helvetica", 12))
        self.__peso.pack(pady=5)
        self.ealtura = tk.Label(self.master, text="Altura (cm):", font=("Helvetica", 12), bg='#f0f0f0')
        self.ealtura.pack(pady=5)
        self.__altura = tk.Entry(self.master, width=20, font=("Helvetica", 12))
        self.__altura.pack(pady=5)
        self.btn_calcular = tk.Button(self.master, text="Calcular", command=self.calcular, font=("Helvetica", 12), bg='#f0f0f0')
        self.btn_calcular.pack(side=tk.LEFT, padx=5, pady=5)
        self.btn_borrar = tk.Button(self.master, text="Borrar", command=self.borrar, font=("Helvetica", 12), bg='#f0f0f0')
        self.btn_borrar.pack(side=tk.RIGHT, padx=5, pady=5)
        
        self.background=tk.Label(self.master, width=10,bg='green')
        self.background.pack(side=BOTTOM, fill=tk.BOTH, expand=True)
        self.texto = tk.Label(self.master, text="Tu indice de masa corporal (imc) es de", font=("Helvetica", 12), bg='sea green')
        self.texto.place(x=82, y=280)
        self.__imc=tk.Label(self.master, text="", font=("Helvetica", 10), bg='green')
        self.__imc.place(x=360, y=280)
        self.__tipo = tk.Label(self.master, text="", font=("Helvetica", 12), bg='green')
        self.__tipo.place(x=230, y=300)
        
    def borrar(self):
        self.__peso.delete(0, tk.END)
        self.__altura.delete(0, tk.END)
        self.__imc.configure(text="")
        self.__tipo.configure(text="")
    def calcular(self):
        if self.__peso.get()!='' and self.__altura.get()!='':
            try:
                peso = float(self.__peso.get())
                print(peso)
                altura = float(self.__altura.get())
                print(altura)
                resultado = peso/ (altura ** 2)
                imc = round(resultado, 2)
                self.__imc.configure(text=imc)
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Debe ingresar un valor numérico')
            
        if imc < 18.5:
            self.__tipo.configure(text="Peso inferior al Normal")
        elif imc >= 18.5 and imc < 25:
            self.__tipo.configure(text="Normal")
        elif imc >= 25 and imc < 30:
            self.__tipo.configure(text="Peso superior al normal")
        elif imc >= 30:
            self.__tipo.configure(text="Obesidad")
        self.master.mainloop()
    
if __name__ == '__main__':
    app=IMC()