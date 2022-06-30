from ClassPaciente import Paciente
from claseManejadorPacientes import ManejadorPacientes
from claseObjectEncoder import ObjectEncoder
from claseRepositorioPacientesJSON import RespositorioPacientes
from vistaPacientes import PacienteList, PacientsView
from claseControladorPacientes import ControladorPacientes
   
if __name__=='__main__':
    json = ObjectEncoder('pacientes.json')
    manejador=ManejadorPacientes()
    diccionario=json.leerJSONArchivo()
    manejador=json.decodificarDiccionario(diccionario)
    repo=RespositorioPacientes(json)
    vista=PacientsView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
    #diccionarioManejador=manejador.toJSON()
    #jF.guardarJSONArchivo(diccionarioManejador, 'contactos.json')

