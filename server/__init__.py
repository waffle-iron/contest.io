from flask import Flask, render_template, jsonify, request, g, session, redirect, url_for
from werkzeug.routing import BaseConverter
import requests, json
from flask_github import GitHub
from .api.problems import getProblems
import .settings as settings

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__,
            static_folder = "../client/dist/static",
            template_folder = "../client/dist")
# Flask app config
app.config['GITHUB_CLIENT_ID'] = settings.GITHUB_CLIENT_ID
app.config['GITHUB_CLIENT_SECRET'] = settings.GITHUB_CLIENT_SECRET

app.url_map.converters['regex'] = RegexConverter


# Github-Flask
github = Github(app)


@app.route('/')
def index():
    if app.debug:
        return requests.get('http://localhost:3000/index.html').text
    return render_template("index.html")

@app.route('/github-login')
def auth_GithubLogin():
    return github.authorize()

@app.route('/github-callback')
@github.authorized_handler
def auth_GithubCallback(auth_token):
    next_url = request.args.get('next') or url_for('index')
    if oauth_token is None:
        flash("Authorization failed.")
        return redirect(next_url)

    user = 
    if user is None:
        user = User(oauth_token)
        db_session.add(user)

    user.github_access_token = oauth_token
    db_session.commit()
    return redirect(next_url)

# TODO: Query with tags as parameters
# TODO: Database Connection - #15, #16, #17
@app.route('/api/problems')
def problemset():
    return json.dumps(getProblems('graphs'))

@app.route('/sockjs-node/<path>')
def sockjs():
    if app.debug:
        return requests.post('http://localhost:3000/sockjs-node/{}'.format(path))
    return render_template("index.html")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:3000/{}'.format(path)).text
    return render_template("index.html")
    