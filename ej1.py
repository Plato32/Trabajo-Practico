import tkinter as tk
from tkinter import BOTTOM, messagebox
from turtle import width

class IMC:
    __altura: float
    __peso: float
    __imc: float
    __tipo: str
    def __init__(self, master):
        self.master = master
        self.master.title("idice de masa corporal")
        self.master.geometry("500x400")
        self.master.resizable(False, False)
        self.master.background = 'beige'
        self.crear_widgets()
    def crear_widgets(self):
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
def main():
    root = tk.Tk()
    app = IMC(root)
    root.mainloop()
if __name__ == '__main__':
    main()

    


'''Ejercicio 1
Una nutricionista hace un análisis rápido de sus pacientes para determinar 
el tratamiento a seguir utilizando el índice de masa corporal (IMC). 

El mismo se calcula con la siguiente fórmula:

IMC = peso [kg]/ estatura2 [m]

Una vez determinado el IMC, 
se puede averiguar la composición corporal utilizando la siguiente tabla:

Composición corporal

Índice de masa corporal (IMC)

Peso inferior al normal

Menos de 18.5

Normal

18.5 – 24.9

Peso superior al normal

25.0 – 29.9

Obesidad       

Más de 30.0

Con esta información la nutricionista puede decidir el tipo de dieta, actividad física y demás tratamientos a recomendar.

Se le solicita a usted que desarrolle una aplicación que permita calcular el IMC e informar la composición corporal.
 Para ello, la nutricionista le ha proporcionado un prototipo de la aplicación que desea.'''

