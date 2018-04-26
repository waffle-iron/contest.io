from flask import Flask, render_template, jsonify, request
from werkzeug.routing import BaseConverter
import server.api.APIConnector as APIConnector
import requests
import json


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


# TODO: Database Connection - #15, #16, #17
@app.route('/api/tasks')
def api_tasks():
    def queryparam_tags(x): return request.args.get(
        'tags') if request.args.get('tags') else None
    respond_rawdata = TasksEndpoint.get(tags=queryparam_tags(None))
    return json.dumps(respond_rawdata)


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
