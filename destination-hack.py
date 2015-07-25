from flask import Flask, jsonify, request, g, render_template
from sqlalchemy import create_engine
from model import connect_db, create_user, get_all_users, get_user
from json import JSONEncoder, JSONDecoder, dumps
from uuid import uuid4

app = Flask(__name__)


@app.route('/destihack/getallusers')
def getusers():
    return dumps({"users": get_all_users()})


@app.route('/destihack/get_user')
def getuser():
    return dumps({"user": get_user(request.args['uid'])})


@app.route('/destihack/login', methods=['POST'])
def newuser():
    incoming_user = request.get_json(force=True)
    user = create_user(int(uuid4().int >> 70), incoming_user['gid'], incoming_user['fname'],
                       incoming_user['lname'], incoming_user['email'], incoming_user['gender'])
    return dumps(user)


@app.route('/destihack/')
@app.route('/destihack/index')
def index():
    return 'Hi. Destihack webapp aanu ithu'


if __name__ == '__main__':
    app.run()
