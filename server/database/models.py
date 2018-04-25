import sqlite3 as sql
import json


def insert_task(name, tags):
    with sql.connect("database.db") as dbcon:
        cur = dbcon.cursor()
        cur.execute(
            "INSERT INTO Task (taskname, tasktags) VALUES (?,?)",
            (name, json.dumps(tags))
        )
        dbcon.commit()
        dbcon.close()


def insert_user(name, usertype, oauth_token):
    with sql.connect("database.db") as dbcon:
        cur = dbcon.cursor()
        cur.execute(
            "INSERT INTO USER (username, usertype, oauth_token) VALUES (?,?,?)",
            (name, usertype, oauth_token)
        )
		dbcon.commit()
		dbcon.close()
		