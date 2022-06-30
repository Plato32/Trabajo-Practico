from ClassPaciente import Paciente
from claseObjectEncoder import ObjectEncoder
from claseManejadorPacientes import ManejadorPacientes
class RespositorioPacientes(object):
    __pacc=None
    __manejador=None
    def __init__(self, pacc):
        self.__pacc = pacc
        diccionario=self.__pacc.leerJSONArchivo()
        self.__manejador=self.__pacc.decodificarDiccionario(diccionario)
    def to_values(self, paciente):
        return paciente.getApellido(), paciente.getNombre(), paciente.getTelefono(),paciente.getAltura(), paciente.getPeso()
    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()
    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente
    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)
    def grabarDatos(self):
        self.__pacc.guardarJSONArchivo(self.__manejador.toJSON())

