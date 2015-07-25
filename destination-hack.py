from flask import Flask, jsonify, request, g, render_template
from sqlalchemy import create_engine
from model import connect_db, create_user, query_user
from json import JSONEncoder, JSONDecoder
from uuid import uuid4

app = Flask(__name__)


@app.before_request
def set_up_db():
    g.db = connect_db()


@app.teardown_request
def close_db(e):
    g.db.close()

@app.route('/destihack/showusers')
def show_entries():
    pass
  #  engine = create_engine('sqlite:///destination.db')
  #  connection = engine.connect()
  #  results = connection.execute("select * from users")
  #  connection._commit_impl(autocommit=True)
  #  x = [row for row in results]
  #  print x[0]
  #  results.close()
  #  return jsonify(x[0])


@app.route('/destihack/newuser', methods=['POST'])
def newuser():
    incoming_user = request.get_json(force=True)
    user = query_user(g.db, incoming_user['gid'])
    if user == None:
        user = create_user(g.db, int(uuid4().int >> 70), incoming_user['gid'], incoming_user['fname'],
                           incoming_user['lname'],
                           incoming_user['email'], incoming_user['gender'])
    return ''


@app.route('/destihack/')
@app.route('/destihack/index')
def index():
    return 'Hi. Destihack webapp aanu ithu'


if __name__ == '__main__':
    app.run()
