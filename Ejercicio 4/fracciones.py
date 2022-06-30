class Fraccion:
    __num=None
    __den=None

    def __init__(self, num, dem):
        if dem != 0:
            self.__num=num
            self.__den=dem
    def __add__(self, otro):
        if type(self)==type(otro):
            print("primer numerador",self.__num)
            print("primer denomindador",self.__den),
            print("otro numerador",otro.__num)
            print("otro denominador",otro.__den)
            denominador=self.__den*otro.__den
            numerador=self.__num*otro.__den+otro.__num*self.__den
            return Fraccion(numerador, denominador).simplificar()
    def __sub__(self, otro):
        if type(self)==type(otro):
            denominador=self.__den*otro.__den
            numerador=self.__num*otro.__den-otro.__num*self.__den
            return Fraccion(numerador, denominador).simplificar()
    def __mul__(self, otro):
        if type(self)==type(otro):
            denominador=self.__den*otro.__den
            numerador=self.__num*otro.__num
            return Fraccion(numerador, denominador).simplificar()
    def __mod__(self, otro):
        if type(self)==type(otro):
            denominador=self.__den*otro.__num
            numerador=self.__num*otro.__den
            return Fraccion(numerador, denominador).simplificar()

    def simplificar(self):
        aux = 0
        a=self.__num
        b=self.__den
        while b != 0:
            aux = b
            b = a % b
            a = aux
        self.__num//=a
        self.__den//=a
        return self

    def getnumerador(self):
        return self.__num

    def getdenominador(self):
        return self.__den

    def __str__(self):
        return ("{}/{}".format(self.__num, self.__den))
       
