import requests, json

def getProblems(tags = None):
	if tags != None:
		return requests.get('http://codeforces.com/api/problemset.problems', params = dict(tags = tags)).json()
	else:
		return requests.get('http://codeforces.com/api/problemset.problems').json()