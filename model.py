from sqlite3 import connect
import datetime
from sqlalchemy import create_engine
from json import dumps


def connect_db():
    return connect("destination.db")


def create_user(uid, gid, fname, lname, email, gender):
    engine = create_engine('sqlite:///destination.db')
    connection = engine.connect()
    user = get_user(gid)
    if user == None:
        query = "INSERT INTO users VALUES ({},{},{},{},{},{})".format(int(uid), gid, fname, lname, gender, email)
        results = connection.execute(query)
        connection._commit_impl(autocommit=True)
        results.close()
        return {"user": get_user(uid), "exists": False}
    return {"user": user, "exists": True}


def get_user(uid):
    engine = create_engine('sqlite:///destination.db')
    connection = engine.connect()
    results = connection.execute("select * from users where uid={}".format(uid))
    connection._commit_impl(autocommit=True)
    user = results._fetchone_impl()
    results.close()
    return user


def get_all_users():
    engine = create_engine('sqlite:///destination.db')
    connection = engine.connect()
    results = connection.execute("select * from users")
    connection._commit_impl(autocommit=True)
    users = results._fetchall_impl()
    results.close()
    return users
