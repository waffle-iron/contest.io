import requests
import json
from server.api.EndpointInterface import EndpointInterface
import server.database.models as models

CODEFORCES_BASE_URL = 'http://codeforces.com/api'


class Tasks(EndpointInterface):
    endpointURL = '/api/tasks'

    def __init__(self):
        self.rawdata = {}
        self.problems = []

    def get(self, tags=None):
        try:
            if tags != None:
                self.rawdata = (requests.get(
                                            '{}/problemset.problems'.format(CODEFORCES_BASE_URL),
                                            params=dict(tags=str(tags)),
                                            allow_redirects=False,
                                            stream=True)
                                        .json())
            else:
                self.rawdata = requests.get(
                    '{}/problemset.problems'.format(CODEFORCES_BASE_URL)).json()
        except requests.exceptions.RequestException as e:
            return e
        else:
            self.extractProblems()
            self.insertToDatabase()
            return self.rawdata['result']['problems']

    def extractProblems(self):
        try:
            if self.rawdata:
                self.problems = self.rawdata['result']['problems']
        except Exception as e:
            print(e)

    def insertToDatabase(self):
        if self.problems:
            for problem in self.problems:
                contestId, index, name, tags = problem['contestId'], problem[
                    'index'], problem['name'], problem['tags']
                url = "http://codeforces.com/problemset/problem/{}/{}".format(
                    contestId, index)
                models.insert_task(
                    name,
                    tags,
                    url,
                )
