from flask import Flask, jsonify, request, g, render_template
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route('/destihack/putuser', methods=['POST'])
def put():
    json_string = request.get_json(force=True)
    print json_string
    return ''


@app.route('/destihack/getdb')
def getsomedb():
    return 'Done'


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


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


@app.route('/destihack/newuser')
def newuser():
    user = {'name': 'Ajay', 'surname': 'Bhat', 'age': '22'}
    return jsonify(user)


@app.route('/destihack/')
@app.route('/destihack/index')
def index():
    return 'Hi. Destihack webapp aanu ithu'


if __name__ == '__main__':
    app.run()
