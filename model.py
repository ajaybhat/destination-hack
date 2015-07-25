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


def create_user(uid, gid, name, email):
    user = get_user_with_gid(gid)
    if user is None:
        query = "INSERT INTO users VALUES ({},'{}','{}','{}')".format(int(uid), gid, name, email)
        results = execute_query(query)
        results.close()
        return {"user": get_user(uid), "exists": False}
    return {"user": user, "exists": True}


def get_all_users():
    results = execute_query("SELECT * FROM users")
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


def get_user_with_gid(gid):
    results = execute_query("SELECT * FROM users WHERE gid='{}'".format(gid))
    user = results._fetchone_impl()
    results.close()
    return user


def get_user(uid):
    results = execute_query("SELECT * FROM users WHERE uid={}".format(uid))
    user = results._fetchone_impl()
    results.close()
    return user


def get_review(place_id, uid):
    results = execute_query("SELECT * FROM reviews WHERE place_id={} AND uid={}".format(place_id, uid))
    review = results._fetchone_impl()
    results.close()
    return review


def get_place(place_id):
    results = execute_query("SELECT * FROM places WHERE place_id={}".format(place_id))
    place = results._fetchone_impl()
    results.close()
    return place


def create_review(rid, place_id, uid, rating, review, score, sentiment):
    review = get_review(place_id, uid)
    if review is None:
        query = "INSERT INTO reviews VALUES ({},{},{},{},{})".format(rid, place_id, rating, review, score, sentiment)
        results = execute_query(query)
        results.close()
        return get_review(place_id, uid)
    return review


def get_interest(uid, tag_id):
    results = execute_query("SELECT * FROM interests WHERE uid={} AND tag_id={}".format(uid, tag_id))
    review = results._fetchone_impl()
    results.close()
    return review

def get_tag_id(tag):
    results = execute_query("SELECT * FROM tags WHERE tag='{}'".format(tag))
    tag = results._fetchone_impl()
    results.close()
    return tag[0]


def create_interests(uid, tags):
    interests = []
    for tag in tags:
        interests.append(get_tag_id(tag))
    for interest in interests:
        result = get_interest(uid, interest)
        if result is None:
            query = "INSERT INTO interests VALUES ({},{})".format(uid, interest)
            results = execute_query(query)
            results.close()

def get_interests(uid):
    results = execute_query("SELECT tag FROM tags where tag_id in (SELECT tag_id FROM interests WHERE uid={})".format(uid))
    interests = results._fetchall_impl()
    results.close()
    return interests


def add_follower(uid1, uid2):
    results = execute_query("INSERT INTO followers VALUES ({},{})".format(uid1, uid2))
