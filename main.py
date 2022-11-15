from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception




app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorResultado import ControladorResultado


miControladorMesa=ControladorMesa()
miControladorPartido=ControladorPartido()
miControladorCandidato=ControladorCandidato()
miControladorResultado=ControladorResultado()

###################################################################################
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
###################################################################################
@app.route("/Mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/Mesas",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/Mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/Mesas/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/Mesas/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)
###################################################################################
@app.route("/partidos",methods=['GET'])
def getpartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)
###################################################################################
@app.route("/candidatos",methods=['GET'])
def getcandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>/Partido/<string:id_Partido>",methods=['PUT'])
def asignarPartidoACandidato(id,id_Partido):
    json=miControladorCandidato.asignarPartido(id,id_Partido)
    return jsonify(json)


#############################RESULTADOS#############################

@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)

""" Asignacion Mesa y Candidato a resultado   """


@app.route("/resultados/Mesa/<string:id_Mesa>/Candidato/<string:id_Candidato>",methods=['POST'])
def crearResultado(id_Mesa,id_Candidato):
    data = request.get_json()
    json=miControladorResultado.create(data,id_Mesa,id_Candidato)
    return jsonify(json)


""" Modificación de Resultado (Mesa y Candidato) """

@app.route("/resultados/<string:id_Resultado>/Mesa/<string:id_Mesa>/Candidato/<string:id_Candidato>",methods=['PUT'])
def modificarResultado(id_Resultado,id_Mesa,id_Candidato):
    data = request.get_json()
    json=miControladorResultado.update(id_Resultado,data,id_Mesa,id_Candidato)
    return jsonify(json)


@app.route("/resultados/<string:id_Resultado>",methods=['DELETE'])
def eliminarResultado(id_Resultado):
    json=miControladorResultado.delete(id_Resultado)
    return jsonify(json)

@app.route("/resultados/candidato/<string:id_Candidato>",methods=['GET'])
def resultadosEnCandidato(id_Candidato):
    json=miControladorResultado.listarResultadosEnCandidato(id_Candidato)
    return jsonify(json)


@app.route("/resultados/Mesas/<string:id_Mesa>",methods=['GET'])
def resultadosEnMesa(id_Mesa):
    json=miControladorResultado.listarResultadosporMesa(id_Mesa)
    return jsonify(json)


@app.route("/resultados/votos_mayores",methods=['GET'])
def getMayorvotoCandidato():
    json=miControladorResultado.Resultadovotacion()
    return jsonify(json)




@app.route("/resultados/promedio_notas/Candidato/<string:id_Candidato>",methods=['GET'])
def getPromedioNotasEnCandidato(id_Candidato):
    json=miControladorResultado.promedioNotasEnCandidato(id_Candidato)
    return jsonify(json)



###################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])