from sqlite3 import connect
import datetime

def connect_db():
	return connect("destination.db")

def create_user(db, uid, gid, fname, lname, email, gender):
    c = db.cursor()
    query = """INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)"""
    result = c.execute(query, (uid, gid, fname, lname, email, gender))
    db.commit()
    return result.lastrowid