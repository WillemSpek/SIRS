from app import app


@app.route('/<id>')
def get_id(id):
    return 'Hello World'