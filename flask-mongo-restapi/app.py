from datetime import datetime
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId


app = Flask(__name__)
app.secret_key = 'secret key'
app.config["MONGO_URI"] = 'mongodb://oport_teste:s3cretp4assw0rd@vm-debian-10-docker:27017/oportunidade_teste'
mongo = PyMongo(app)


@app.route('/oportunidade')
def oportunidades():
    oports = mongo.db.selecoes.find()
    resp = dumps(oports)
    return resp


@app.route('/oportunidade/<id>')
def oportunidade(id):
    oport = mongo.db.selecoes.find_one({'_id': ObjectId(id)})
    resp = dumps(oport)
    return resp


@app.route('/oportunidade', methods=['POST'])
def add_oportunidade():
    _json = request.json
    _titulo = _json['titulo']
    _descricao = _json['descricao']
    _uf = _json['uf']
    _periodo_inscricao = _json['periodoInscricao']
    _link = _json['link']
    _enviado = _json['enviado']
    _hash = _json['hash']
    _data_cadastro = datetime.utcnow()

    id = mongo.db.selecoes.insert({'titulo': _titulo, 'descricao': _descricao, 'uf': _uf, 'periodoInscricao': _periodo_inscricao,
                                   'link': _link, 'enviado': _enviado, 'hash': _hash, 'dataCadastro': _data_cadastro})

    resp = None
    if id is not None:
        resp = jsonify('Oportunidade adicionada!')
        resp.status_code = 201
    else:
        resp = jsonify('Erro ao adicionar!')
        resp.status_code = 500
    return resp


"""
@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
    # validate the received values
    if _name and _email and _password and request.method == 'POST':
        # do not save password as a plain text
        _hashed_password = generate_password_hash(_password)
        # save details
        id = mongo.db.user.insert(
            {'name': _name, 'email': _email, 'pwd': _hashed_password})
        resp = jsonify('User added successfully!')
        resp.status_code = 200
        return resp
    else:
        return not_found()
"""


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()
