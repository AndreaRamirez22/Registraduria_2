from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        print(self.repositorioResultado)
        self.repositorioMesas = RepositorioMesa()
        print(self.repositorioMesas)
        self.repositorioCandidatos = RepositorioCandidato()
        print(self.repositorioCandidatos)

    def index(self):
        return self.repositorioResultado.findAll()

    """  Asignacion Mesa y Candidato a resultado     """

    def create(self,infoResultado,id_Mesa,id_Candidato):
        nuevaResultado=Resultado(infoResultado)
        laMesa=Mesa(self.repositorioMesas.findById(id_Mesa))
        elcandidato=Candidato(self.repositorioCandidatos.findById(id_Candidato))
        nuevaResultado.Mesa=laMesa
        nuevaResultado.Candidato=elcandidato
        return self.repositorioResultado.save(nuevaResultado)

    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de Resultado (Mesa y Candidato)
    """
    def update(self,id,infoResultado,id_Mesa,id_Candidato):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_mesa=infoResultado["numero_mesa"]
        elResultado.cedula_candidato = infoResultado["cedula_candidato"]
        elResultado.numero_votos=infoResultado["numero_votos"]
        laMesa = Mesa(self.repositorioMesas.findById(id_Mesa))
        elcandidato = Candidato(self.repositorioCandidatos.findById(id_Candidato))
        elResultado.Mesa = laMesa
        elResultado.Candidato = elcandidato
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)


    "Obtener todos los Resultados de un Candidato"
    def listarResultadosEnCandidato(self,id_Candidato):
        return self.repositorioResultado.getListadoResultadosEnCandidato(id_Candidato)


    "Obtener todos los Resultados por Mesa"
    def listarResultadosporMesa(self,id_Mesa):
        return self.repositorioResultado.getListadoResultadosporMesa(id_Mesa)

    "Obertener Partidos Politicos con cantidad de votos"

    def Resultadovotacion(self):
        return self.repositorioResultado.getMayorvotoCandidato()

    def Resultadovotacion(self):
        return self.repositorioResultado.getMayorvotoCandidato()












"""""""""""
    "Obtener votos mas altos por candidato"
    def votosmasAltosPorCandidato(self):
            return self.repositorioResultado.getMayorvotoCandidato()

    "Obtener Total por Candidato"

    def sumaMesasxCandidato(self):
        return self.repositorioResultado.getTotalVotosxCandidato()


    "Obtener votos mas altos por candidato"
    def votosmasAltosPorCandidato(self):
            return self.repositorioResultado.getMayorvotoCandidato()


    "Obtener promedio de notas en Candidato"
    def promedioNotasEnCandidato(self,id_Candidato):
        return  self.repositorioResultado.promedioNotasEnCandidato(id_Candidato)

"""""""""""