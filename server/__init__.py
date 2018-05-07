from flask import Flask, render_template, jsonify, request, g, session, redirect, url_for, flash
from werkzeug.routing import BaseConverter
import requests
import json
import flask_github
import server.api.APIConnector as APIConnector
import server.database.models as models
import server.settings as settings


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__,
            static_folder="../client/dist/static",
            template_folder="../client/dist")
# Flask app config
app.config['GITHUB_CLIENT_ID'] = settings.GITHUB_CLIENT_ID
app.config['GITHUB_CLIENT_SECRET'] = settings.GITHUB_CLIENT_SECRET

app.url_map.converters['regex'] = RegexConverter

# Set Endpoints
TasksEndpoint = APIConnector.Tasks()

# Github-Flask
github = flask_github.GitHub(app)


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = models.select_user(conditions=(
            "{}={}".format(settings.DB_COLUMNS.USER_USERID, session['user_id'])))


@app.route('/')
def index():
    if app.debug:
        return requests.get('http://localhost:3000/index.html').text
    return render_template("index.html")


@app.route('/github-login')
def auth_GithubLogin():
    if session.get('user_id', None) is None:
    return github.authorize()


# TODO: Github Callback
@app.route('/github-callback')
@github.authorized_handler
def auth_GithubCallback(auth_token):
    next_url = request.args.get('next') or url_for('index')
    # if oauth_token is None:
    #     flash("Authorization failed.")
    #     return redirect(next_url)

    # user = models.select_user(params=())
    # if user is None:
    #     user = User(oauth_token)
    #     db_session.add(user)

    # user.github_access_token = oauth_token
    # db_session.commit()
    return redirect(next_url)


@app.route('/api/tasks', methods=['GET', 'POST'])
def api_tasks():
    if request.method == 'GET':
        returnJSON = None

        def queryparam_tags(x): return request.args.get(
            'tags') if request.args.get('tags') else None

        if queryparam_tags(None) != None:
            tasks_in_database = models.select_task(conditions=(
                "tasktags LIKE '%{}%'".format(queryparam_tags(None))))

        if tasks_in_database is not None:
            returnJSON = tasks_in_database
        else:
            respond_rawdata = TasksEndpoint.get(tags=queryparam_tags(None))
            returnJSON = respond_rawdata

        # @FRONT-END tasktags have to be parsed -> JSON.parse
        return json.dumps(returnJSON)
    else:
        return None


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
