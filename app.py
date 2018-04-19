from flask import Flask, render_template
app = Flask(__name__,
            static_folder = ".client/dist/static",
            template_folder = ".client/dist")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")