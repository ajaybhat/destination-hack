from json import dumps
from flask import Flask, request
from uuid import uuid4
from model import create_user, get_all_users, get_user, create_interests, get_interests

app = Flask(__name__)

@app.route('/destihack/getallusers')
def getusers():
    return dumps({"users": get_all_users()})


@app.route('/destihack/get_user')
def getuser():
    return dumps({"user": get_user(request.args['uid'])})

@app.route('/destihack/interests',methods=['POST'])
def interests():
    incoming_payload = request.get_json(force=True)
    create_interests(incoming_payload['uid'],incoming_payload['interests'])
    return ''

@app.route('/destihack/get_interests')
def getinterests():
    return dumps({"interests": get_interests(int(request.args['uid']))})



@app.route('/destihack/login', methods=['POST'])
def newuser():
    incoming_user = request.get_json(force=True)
    user = create_user(int(uuid4().int >> 70), incoming_user['gid'], incoming_user['name'], incoming_user['email'])
    return dumps(user)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

