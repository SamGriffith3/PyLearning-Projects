# Imports
from flask import Flask, url_for
import urllib.request

app = Flask(__name__)


# Views
@app.route('/')


@app.route('/index')
def index():
    return "It worked!"


@app.route('/user_input')
def user_input():
    return "working on it"


@app.route('/last_ten')
def last_ten():
    return "also, working on it"


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid


@app.route('/page1')
def page1():
    r = login.html

    return r



# Start Server
app.run(debug=True)


