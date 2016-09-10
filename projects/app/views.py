from app import app

@app.route('/')
@app.route('/input')
def input():
    return "Hey Partner"

