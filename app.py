from flask import Flask, render_template
import requests


app = Flask(__name__,
            static_folder = "./client/dist/static",
            template_folder = "./client/dist")


@app.route('/')
def index():
    if app.debug:
        return requests.get('http://localhost:8080/index.html').text
    return render_template("index.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")