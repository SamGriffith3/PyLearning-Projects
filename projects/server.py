from flask import Flask
app = Flask(__name__)

@app.route(8080, '/')
def hello_world():
    return 'Hello, World!'