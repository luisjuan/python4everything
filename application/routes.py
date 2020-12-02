from application import app


@app.route('/')
def index():
    return 'Hello, Python4Everyone!'