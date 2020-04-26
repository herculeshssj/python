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


@app.route('/oportunidade', methods=['PUT'])
def update_oportunidade():
    _json = request.json
    _id = _json['_id']
    _titulo = _json['titulo']
    _descricao = _json['descricao']
    _uf = _json['uf']
    _periodo_inscricao = _json['periodoInscricao']
    _link = _json['link']
    _enviado = _json['enviado']
    _hash = _json['hash']

    mongo.db.selecoes.update_one(
        {'_id': ObjectId(_id['$oid'] if '$oid' in _id else ObjectId(_id))},
        {'$set': {'titulo': _titulo, 'descricao': _descricao, 'uf': _uf,
                  'periodoInscricao': _periodo_inscricao, 'link': _link, 'enviado': _enviado, 'hash': _hash}}
    )

    resp = None
    if id is not None:
        resp = jsonify('Oportunidade atualizada!')
        resp.status_code = 201
    else:
        resp = jsonify('Erro ao atualizar!')
        resp.status_code = 500
    return resp


@app.route('/oportunidade/<id>', methods=['DELETE'])
def delete_oportunidade(id):
    mongo.db.selecoes.delete_one({'_id': ObjectId(id)})
    resp = jsonify('Oportunidade apagada!')
    resp.status_code = 200
    return resp


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
