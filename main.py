from json import dumps
from flask import Flask, request
from uuid import uuid4
from sentment_analysis import sentence_score
from model import create_user, get_all_users, get_user, get_review, create_interests, get_interests, get_follower, \
    search_users, create_review, add_follower, get_followers, get_following

app = Flask(__name__)


@app.route('/destihack/getallusers')
def getusers():
    return dumps({"users": get_all_users()})


@app.route('/destihack/get_user')
def getuser():
    return dumps({"user": get_user(request.args['uid'])})


@app.route('/destihack/review', methods=['POST'])
def review():
    incoming_review = request.get_json(force=True)
    review_text = incoming_review['review_text']
    sentiment_score = sentence_score(review_text)
    create_review(get_uuid(), incoming_review['place_id'], incoming_review['uid'], incoming_review['rating'],
                  incoming_review['review_text'], 0 if sentiment_score < 4 else 1, sentiment_score)
    return ''


@app.route('/destihack/interests', methods=['POST'])
def interests():
    incoming_payload = request.get_json(force=True)
    create_interests(incoming_payload['uid'], incoming_payload['interests'])
    return ''


@app.route('/destihack/follow')
def follow():
    status = add_follower(request.args['uid'], request.args['fid'])
    return dumps({"status": "followed" if status else "already followed"})


@app.route('/destihack/get_followers')
def getfollowers():
    return dumps({"followers": get_followers(request.args['uid'])})


@app.route('/destihack/get_following')
def getfollowing():
    return dumps({"following": get_following(request.args['uid'])})


@app.route('/destihack/get_interests')
def getinterests():
    return dumps({"interests": get_interests(int(request.args['uid']))})


@app.route('/destihack/search_users')
def searchusers():
    return dumps({"search_results": search_users(request.args['name'],int(request.args['uid']))})


@app.route('/destihack/login', methods=['POST'])
def newuser():
    incoming_user = request.get_json(force=True)
    user = create_user(get_uuid(), incoming_user['gid'], incoming_user['name'], incoming_user['email'])
    return dumps(user)


@app.route('/destihack/get_review')
def get_r():
    incoming_user = request.get_json(force=True)
    review = get_review(incoming_user['place_id'], incoming_user['uid'])
    return dumps(review)


def get_uuid():
    return int(uuid4().int >> 70)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
