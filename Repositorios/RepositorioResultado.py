from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):

    def getListadoResultadosEnCandidato(self, id_Candidato):

        theQuery = {"Candidato.$id": ObjectId(id_Candidato)}
        return self.query(theQuery)

    def getListadoResultadosporMesa(self, id_Mesa):

        theQuery = {"Mesa.$id": ObjectId(id_Mesa)}
        return self.query(theQuery)



    def getMayorvotoCandidato(self):
        query1={
                 "$group":{
                    "_id": "$Candidato",
                    "Total_votos_candidato": {
                        "$sum": 1
                },
            "doc": {
                "$first": "$$ROOT"
                }
            }
        }

        pipeline= [query1]
        return self.queryAggregation(pipeline)




def getTotalVotosxCandidato(self):

        query1 = {
            "$group": {
                "_id": "$Candidato",
                "sum": {
                    "$sum": "$numero_votos"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)



"""""""""""

    def promedioNotasEnCandidato(self,id_Candidato):
        query1 = {
          "$match": {"Candidato.$id": ObjectId(id_Candidato)}
        }
        query2 = {
          "$group": {
            "_id": "$Candidato",
            "promedio": {
              "$avg": "$nota_final"
            }
          }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)


"""""""""""