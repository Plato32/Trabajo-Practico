from run import Api


class Provincia:
    __Nombre:str
    __Capital:str
    __Cantidadhabitantes:int
    __Departamentos:int
    __api:str
    def __init__(self, Nombre, Capital, Cantidadhabitantes, Departamentos):
        try:
            self.__Nombre=Nombre
            self.__Capital=Capital
            self.__Cantidadhabitantes=Cantidadhabitantes
            self.__Departamentos=Departamentos
            self.__api=Api()
            url='https://api.openweathermap.org/data/2.5/weather?q='+self.__Capital.replace(" ","+")+'&units=metric&&ang=es&appid=d271ee37a01bfc5239b4db53fb93197e'
            self.__api.run(url)
        except ValueError:
            raise ValueError
    def getNom(self):
        return self.__Nombre
    def getCap(self):
        return self.__Capital
    def getHab(self):
        return self.__Cantidadhabitantes
    def getDep(self):
        return self.__Departamentos
    def getTemp(self):
        return str(self.__api.getResultado()['main']['temp'])
    def getSens(self):
        return str(self.__api.getResultado()['main']['feels_like'])
    def getHum(self):
        return str(self.__api.getResultado()['main']['humidity'])
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                Nombre=self.__Nombre,
                Capital=self.__Capital,
                Cantidadhabitantes=self.__Cantidadhabitantes,
                Departamentos=self.__Departamentos,
                )
            )
        return d