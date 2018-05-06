from flask import Flask, render_template, jsonify, request
from werkzeug.routing import BaseConverter
import requests
import json
import server.api.APIConnector as APIConnector
import server.database.models as models


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app = Flask(__name__,
            static_folder="../client/dist/static",
            template_folder="../client/dist")

app.url_map.converters['regex'] = RegexConverter

TasksEndpoint = APIConnector.Tasks()


@app.route('/')
def index():
    
    if app.debug:
        return requests.get('http://localhost:3000/index.html').text
    return render_template("index.html")


@app.route('/api/tasks', methods=['GET', 'POST'])
def api_tasks():
    if request.method == 'GET':
        returnJSON = None

        def queryparam_tags(x): return request.args.get(
            'tags') if request.args.get('tags') else None
        
        tasks_in_database = models.select_task()

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
