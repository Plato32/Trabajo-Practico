import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
from turtle import width

class Calculador(tk.Tk):
    __ventana=None
    __valorbase = None
    __tipo = None
    __total =None
    __iva = None

    def __init__(self):
        self.__ventana=Tk()
        self.__ventana.title("Calculo de IVA")
        self.__ventana.geometry("500x500")
        self.__ventana.resizable(True, True)

        frame1 = Frame(self.__ventana)
        frame1.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        frame2 = Frame(self.__ventana,bg="")
        self.titulo = tk.Label(frame1, text="Calculo de IVA", font=("Helvetica", 16), bg='lightblue')
        self.titulo.pack(side=TOP, fill=BOTH, expand=True)

        frame2.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        self.__valorbase = StringVar()
        self.evalor = tk.Label(frame2, text="Valor base", font=("Helvetica", 12), bg='white')
        self.evalor.pack(side=tk.LEFT, expand=True)
        self.valor =Entry(frame2, textvariable=self.__valorbase)
        self.valor.pack(side=tk.RIGHT, fill=BOTH, expand=True)

        frame3 = Frame(self.__ventana,bg="")
        frame3.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        self.__iva = StringVar()
        Label(frame3, text="IVA").pack(side=LEFT, fill=BOTH, expand=True,padx=5, pady=5)
        Label(frame3, textvariable=self.__iva).pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)
        self.__tipo = StringVar()
        Radiobutton(frame3, text="IVA 21%", variable=self.__tipo, value=0.21).pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        Radiobutton(frame3, text="IVA 10.5%", variable=self.__tipo, value=0.105).pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        
        frame4 = Frame(self.__ventana,bg="")
        frame4.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
        self.__total = StringVar()
        Label(frame4, text="Total").pack(side=LEFT, fill=BOTH, expand=True,padx=5, pady=5)
        Label(frame4, textvariable=self.__total).pack(side=RIGHT, fill=BOTH, expand=True,padx=5, pady=5)

        frame5 = Frame(self.__ventana,bg="")
        frame5.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5 )
        boton=tk.Button(frame5, text="Calcular", bg="gray",font=("Helvetica", 12),command=self.calcular).pack(side=tk.LEFT)
        botons=tk.Button(frame5, text="Salir", bg="brown",font=("Helvetica", 12),command=self.salir).pack(side=tk.RIGHT)
       

    def ejecutar(self):
        self.__ventana.mainloop()

    def salir(self):
        self.__ventana.destroy()
    def calcular(self):
        if  self.valor.get()!='':
            try:
                valorbase=float(self.valor.get())
                iv=float(self.__tipo.get())
                iva = float(valorbase * iv)
                self.__iva.set(iva)
                self.__total.set(iva+float(self.__valorbase.get()))
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Seleccione un tipo de IVA')
if __name__ == '__main__':
    app=Calculador()
    app.ejecutar()

