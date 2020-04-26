from app import app, mongo


from flask import jsonify, request
from werkzeug import generate_password_hash, check_password_hash


"""

@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.user.delete_one({'_id': ObjectId(id)})
    resp = jsonify('User deleted successfully!')
    resp.status_code = 200
    return resp

"""
