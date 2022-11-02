from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
        # “repositorioMesa” esto servirá para poder acceder a todos los métodos del repositorio#
    def index(self):
        # de listar todos los elementos de la clase correspondiente #
        return self.repositorioMesa.findAll()
    #findall , llamado al repositorio#
    def create(self,infoMesa):
        #encargado de crear nuevos registros#
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,id):
        #el cual por convención para este proyecto será el encargado de mostrar la información de un modelo#
        elMesa=Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__
    def update(self,id,infoMesa):
        MesaActual=Mesa(self.repositorioMesa.findById(id))
        MesaActual.numero=infoMesa["numero"]
        MesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(MesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)