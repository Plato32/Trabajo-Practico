from tkinter import *
from tkinter import ttk, messagebox
import json
from urllib.request import urlopen

class Aplicacion():
    __ventana=None
    __dolares=None
    __pesos=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor de moneda')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__dolares = StringVar()
        self.__pesos = StringVar()
        self.dolaresEntry = ttk.Entry(mainframe, width=7, textvariable=self.__dolares)
        self.dolaresEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__pesos).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="dólares").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="pesos").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.dolaresEntry.focus()
        self.__ventana.mainloop()
    def run(self):
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen(url_template)
        self.resultado = json.loads(response.read().decode())
        dolarventa=float(str(self.resultado[0]['casa']['venta']).replace(",","."))
        return(dolarventa)
    
    def calcular(self):
        try:
            valor=float(self.dolaresEntry.get())
            valordolar=float(self.run())
            self.__pesos.set(2.54*valor)

        except ValueError:
            messagebox.showerror(title='Error de tipo',
                                 message='Debe ingresar un valor numérico')
            self.__dolares.set('')
            self.dolaresEntry.focus()

def testAPP():
    mi_app = Aplicacion()
if __name__ == '__main__':
    testAPP()


