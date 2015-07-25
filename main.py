from json import dumps
from flask import Flask, request
from uuid import uuid4
from model import create_user, get_all_users, get_user,get_follower

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

@app.route('/destihack/get_review')
def get_r():
    incoming_user = request.get_json(force=True)
    review= get_review(incoming_user['place_id'], incoming_user['uid'])
    return dumps(review)

@app.route('/destihack/get_follower')
def get_f():
    incoming_user = request.get_json(force=True)
    follower = get_follower(incoming_user['uid'])
    return dumps(follower)

if __name__ == '__main__':
    app.run()
