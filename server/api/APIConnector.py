import .problems
import requests
import json
from .EndpointInterface import EndpointInterface

CODEFORCES_BASE_URL = 'http://codeforces.com/api'


class Tasks(EndpointInterface):
    def __init__(self):
        self.rawdata = {}
        self.problems = []

    def get(self, tags=None):
        try:
            if tags != None:
                self.rawdata = requests.get(
                    '{}/problemset.problems'.format(CODEFORCES_BASE_URL), params=dict(tags=tags)).json()
            else:
                self.rawdata = requests.get(
                    '{}/problemset.problems'.format(CODEFORCES_BASE_URL)).json()
        except requests.exceptions.RequestException as e:
            return e
        else:
            self.extractProblems()
            return self.rawdata

    def extractProblems(self):
        try:
            if self.rawdata:
                self.problems = self.rawdata.result.problems
        except Exception as e:
            print(e)
