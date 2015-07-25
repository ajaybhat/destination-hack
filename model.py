from sqlite3 import connect
import datetime
from sqlalchemy import create_engine
from json import dumps


def connect_db():
    return connect("destination.db")


def execute_query(query):
    engine = create_engine('sqlite:///destination.db')
    connection = engine.connect()
    results = connection.execute(query)
    connection._commit_impl(autocommit=True)
    return results


def create_user(uid, gid, fname, lname, email, gender):
    user = get_user(gid)
    if user == None:
        query = "INSERT INTO users VALUES ({},{},{},{},{},{})".format(int(uid), gid, fname, lname, gender, email)
        results = execute_query(query)
        results.close()
        return {"user": get_user(uid), "exists": False}
    return {"user": user, "exists": True}


def get_user(uid):
    results = execute_query("select * from users where uid={}".format(uid))
    user = results._fetchone_impl()
    results.close()
    return user


def get_all_users():
    results = execute_query("select * from users")
    users = results._fetchall_impl()
    results.close()
    return users


def get_place_reviews(place_id):
    results = execute_query("SELECT * FROM reviews WHERE place_id={}".format(place_id))
    reviews = results._fetchall_impl()
    results.close()
    return reviews


def get_places_visited(uid):
    results = execute_query("SELECT * FROM visited WHERE uid={}".format(uid))
    places = results._fetchall_impl()
    results.close()
    return places


