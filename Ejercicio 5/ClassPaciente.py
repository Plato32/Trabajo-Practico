class Paciente:
    __Nombre:str
    __Apellido:str
    __Telefono:str 
    __Altura:int
    __Peso:int
    def __init__(self, Apellido, Nombre, Telefono, Altura, Peso):
        self.__Nombre = self.requerido(Nombre, 'Nombre es un valor requerido')
        self.__Apellido = self.requerido(Apellido, 'Apellido es un valor requerido')
        self.__Telefono = self.requerido(Telefono, 'Telefono es un valor requerido')
        self.__Altura = self.requerido(Altura, 'Altura es un valor requerido')
        self.__Peso = self.requerido(Peso, 'Peso es un valor requerido')
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def getNombre(self):
        return self.__Nombre
    def getApellido(self):
        return self.__Apellido
    def getTelefono(self):
        return self.__Telefono
    def getAltura(self):
        return self.__Altura
    def getPeso(self):
        return self.__Peso
    def getimc(self):
        imc=int(self.__Peso) / (int(self.__Altura) / 100) ** 2
        redondeado=round(imc,2)
        return redondeado
    def gettipo(self):
        imc=self.getimc()
        print(imc)
        char=""
        if imc < 18.5:
            char= "Peso bajo"
        elif imc < 25:
            char= "Peso normal"
        elif imc < 30:
            char= "Peso superior al normal"
        else:
            char= "Obesidad"
        return(char)
    def setNombre(self, nombre):
        self.__Nombre = nombre
    def setApellido(self, apellido):
        self.__Apellido = apellido
    def setTelefono(self, telefono):
        self.__Telefono = telefono
    def setAltura(self, altura):
        self.__Altura = altura
    def setPeso(self, peso):
        self.__Peso = peso
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                                    Apellido=self.__Apellido,
                                    Nombre=self.__Nombre,
                                    Telefono=self.__Telefono,
                                    Altura=self.__Altura,
                                    Peso=self.__Peso
                                )
                )
        return d
    def __str__(self):
        return "Nombre: " + self.__Nombre + "\nApellido: " + self.__Apellido + "\nTeléfoono: " + self.__Telefono + "\nAltura: " + str(self.__Altura) + "\nPeso: " + str(self.__Peso) + "\nIMC: " + str(self.get_imc) + "\nTipo: " + self.__tipo