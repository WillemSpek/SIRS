from app import app, mongodb_client, db
from flask import jsonify, make_response, redirect, request, url_for


@app.route('/<id>', methods=['GET'])
def get_id(id):

    record = db.audting_companies.find_one({'id': id})
    if not record:
        return make_response('Id not found', 400)   

    return jsonify(record, 200)