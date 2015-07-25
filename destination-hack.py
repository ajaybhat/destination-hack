from flask import Flask, jsonify, request, g, render_template
from sqlalchemy import create_engine
from model import connect_db, create_user
from json import JSONEncoder, JSONDecoder
from uuid import uuid4

app = Flask(__name__)

@app.before_request
def set_up_db():
    g.db = connect_db()


@app.teardown_request
def close_db(e):
    g.db.close()


@app.route('/destihack/putuser', methods=['POST'])
def put():
    json_string = request.get_json(force=True)
    print json_string
    return ''


@app.route('/destihack/showusers')
def show_entries():
    engine = create_engine('sqlite:///destination.db')
    connection = engine.connect()
    results = connection.execute("select * from users where uid=1")
    connection._commit_impl(autocommit=True)
    x = [row for row in results]
    print x[0]
    results.close()
    return x[0]


@app.route('/destihack/newuser', methods=['POST'])
def newuser():
    incoming_user = request.get_json(force=True)
    user = create_user(g.db, uuid4().int>>64, incoming_user['gid'], incoming_user['fname'], incoming_user['lname'],
                       incoming_user['email'], incoming_user['gender'])
    return jsonify(user)


@app.route('/destihack/')
@app.route('/destihack/index')
def index():
    return 'Hi. Destihack webapp aanu ithu'


if __name__ == '__main__':
    app.run()
