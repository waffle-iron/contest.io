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
            # convert one-value tuples to real tuples
            if not isinstance(params, tuple):
                params = (params,)
            if not isinstance(conditions, tuple):
                conditions = (conditions,)

            if params != ():
                queryString = "SELECT"
                # add a format-placeholder for every parameter
                for paramString in params:
                    queryString += " {},".format(paramString)
                queryString = queryString[:-1]
                queryString += " FROM User"
            if conditions != ():
                queryString += " WHERE"
                for conditionString in conditions:
                    queryString += " {} AND".format(conditionString)
                queryString = queryString[:-4]
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
            # convert one-value tuples to real tuples
            if not isinstance(params, tuple):
                params = (params,)
            if not isinstance(conditions, tuple):
                conditions = (conditions,)

            if params != ():
                queryString = "SELECT"
                # add a format-placeholder for every parameter
                for paramString in params:
                    queryString += " {},".format(paramString)
                queryString = queryString[:-1]
                queryString += " FROM User"
            if conditions != ():
                queryString += " WHERE"
                for conditionString in conditions:
                    queryString += " {} AND".format(conditionString)
                queryString = queryString[:-4]
            queryresult = cur.execute(queryString)

    response = queryresult.fetchone()
    if not response:
        return None
    else:
        return response


def update_user(updatedValues=(), set_conditions=()):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        if cur.rowcount == 0:
            return None

        if updatedValues == () and set_conditions == ():
            return None
        else:
            # convert one-value tuples to real tuples
            if not isinstance(updatedValues, tuple):
                updatedValues = (updatedValues,)
            if not isinstance(set_conditions, tuple):
                set_conditions = (set_conditions,)

            if updatedValues != ():
                queryString = "UPDATE User SET"
                # add a format-placeholder for every parameter
                for updateString in updatedValues:
                    queryString += " {},".format(updateString)
                queryString = queryString[:-1]
            if set_conditions != ():
                queryString += " WHERE"
                for conditionString in set_conditions:
                    queryString += " {} AND".format(conditionString)
                queryString = queryString[:-4]
            cur.execute(queryString)


def delete_user(delete_conditions=()):
    with sql.connect(DATABASE_PATH) as dbcon:
        cur = dbcon.cursor()
        if cur.rowcount == 0:
            return None
        if delete_conditions == ():
            return None
        else:
            if not isinstance(delete_conditions, tuple):
                delete_conditions = (delete_conditions,)

            queryString = "DELETE FROM User WHERE"
            for conditionString in delete_conditions:
                queryString += " {} AND".format(conditionString)
            queryString = queryString[:-4]
            cur.execute(queryString)
