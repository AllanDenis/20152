from flask import Flask, jsonify, request
from flask.ext.cors import CORS
from flask.ext.compress import Compress
import matricula, modelo

app = Flask(__name__)
CORS(app)
Compress(app)

@app.route('/disciplinas', methods = ['GET'])
def lista_disciplinas():
    disciplinas = []
    for d in modelo.Disciplina.select():
        disc_tmp = {
            "id"        :   d.id,
            "nome"      :   d.nome,
            "sigla"     :   d.sigla,
            "periodo"   :   d.periodo,
            "ativa"     :   d.ativa,
        }
        disciplinas.append(disc_tmp)
    return jsonify(enumerate(disciplinas))

@app.route('/grade', methods = ['POST'])
def melhor_grade():
    if request.json:
        return "Dados informados (POST): " + str([d for d in request.json]) + '\n'
    else:
        return None

if __name__ == '__main__':
    app.debug = True
    app.use_reloader = True
    app.run(host='0.0.0.0')
