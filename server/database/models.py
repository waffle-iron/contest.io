import sqlite3 as sql
import json
import secrets
import datetime

DATABASE_PATH = "server/database/database.db"


def insert_task(name, tags, url):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        stringified_tags = json.dumps(tags)
        cur.execute(
            "INSERT INTO Task (taskname, tasktags, codeforces_url) VALUES (?,?,?)",
            (name, stringified_tags, url)
        )
        cur.close()
        dbcon.commit()


def select_task(params=(), conditions=()):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        if cur.rowcount == 0:
            return None
        if params == () and conditions == ():
            queryresult = cur.execute("SELECT * FROM Task")
        else:
            queryString = "SELECT"
            # add a format-placeholder for every parameter
            for i in range(len(params) - 1):
                queryString += "{},"
            queryString += "{} FROM Task"
            queryString = queryString.format(params)
            queryString += "WHERE"
            for i in range(len(conditions)):
                queryString += "{} AND"
            queryString = queryString[:-4]
            queryString = queryString.format(conditions)
            queryresult = cur.execute(queryString)

    response = queryresult.fetchall()
    if len(response) == 0:
        return None
    else:
        return response


def insert_contest(name, date_start, date_end, visible, contestgroup):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        random_code = secrets.token_hex(16)
        date_start = datetime.datetime(*date_start)
        date_end = datetime.datetime(*date_end)
        cur.execute(
            "INSERT INTO Contest (contestcode, contestname, date_start, date_end, visible, contestgroup) VALUES (?,?,?,?,?,?)",
            (random_code, name, date_start, date_end, visible, contestgroup)
        )
        dbcon.commit()


def insert_user(name, usertype, oauth_token):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        cur.execute(
            "INSERT INTO User (username, usertype, oauth_token) VALUES (?,?,?)",
            (name, usertype, oauth_token)
        )
        dbcon.commit()


def select_user(params=(), conditions=()):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        if cur.rowcount == 0:
            return None
        if params == () and conditions == ():
            queryresult = cur.execute("SELECT * FROM User")
        else:
            queryString = "SELECT"
            # add a format-placeholder for every parameter
            for i in range(len(params) - 1):
                queryString += "{},"
            queryString += "{} FROM User"
            queryString = queryString.format(params)
            queryString += "WHERE"
            for i in range(len(conditions)):
                queryString += "{} AND"
            queryString = queryString[:-4]
            queryString = queryString.format(conditions)
            queryresult = cur.execute(queryString)

    response = queryresult.fetchall()
    if len(response) == 0:
        return None
    else:
        return response


def update_user(updatedValues=(), set_conditions=()):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        if cur.rowcount == 0:
            return None

        queryString = "UPDATE User SET"
        # add a format-placeholder for every parameter
        for i in range(len(updatedValues)):
            queryString += "{},"
        queryString = queryString[:-1]
        queryString = queryString.format(updatedValues)
        queryString += "WHERE"
        for i in range(len(set_conditions)):
            queryString += "{} AND"
        queryString = queryString[:-4]
        queryString = queryString.format(set_conditions)

        cur.execute(queryString)