from sqlite3 import connect
import datetime

def connect_db():
	return connect("destination.db")

def create_user(db, uid, gid, fname, lname, email, gender):
    c = db.cursor()
    query = "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)"
    c.execute(query, (uid, gid, fname, lname, email, gender))
    db.commit()
    return query_user(gid)



def query_user(db, gid):
    c = db.cursor()
    query = "SELECT * FROM users where gid = (?)"
    result = c.execute(query,(gid))
    db.commit()
    return result.fetchone()
