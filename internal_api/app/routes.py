from app import app, mongodb_client, db
from flask import jsonify, make_response, redirect, request, url_for

DBNAMES = mongodb_client.list_database_names()


@app.route('/<entry>/<id>', methods=['GET'])
def get_id(entry, id):
    if not entry in DBNAMES:
        return make_response('Invalid database entry', 400)

    entry = getattr(db, entry)
    record = entry.find_one({'id': id})
    if not record:
        return make_response('Id not found', 400)   

    return jsonify(record, 200)


@app.route('/<entry>', methods=['POST'])
def add_id(entry):
    if not entry in DBNAMES:
        return make_response('Invalid request', 400)

    entry = getattr(db, entry)
    params = request.get_json()

    try: 
        record = db.entry.insert_one(params)
    except Exception as exception:
        return make_response('{}'.format(exception), 400)
    return jsonify('Succesfully inserted record with id {}'.format(record), 200)


@app.route('/<entry>/<id>', methods=['PUT'])
def update_id(entry, id):
    if not entry in DBNAMES:
        return make_response('Invalid database entry', 400)

    entry = getattr(db, entry)
    params = request.get_json()

    try: 
        db.entry.update_one(params)
    except Exception as exception:
        return make_response('{}'.format(exception), 400)
    return jsonify('Succes', 200)


@app.route('/<entry>/<id>', methods=['DELETE'])
def delete_id(entry, id):
    if not entry in DBNAMES:
        return make_response('Invalid request', 400)

    entry = getattr(db, entry)
    report = entry.deleteOne({'id': id})
    if not(report['acknowledged']):
        return make_response('Operation Failed', 500)
    if report['deletedCount'] <= 0:
        return make_response('Invalid ID', 400)

    return make_response(f'Succesfully deleted record with  \
                           id: {id}', 204)