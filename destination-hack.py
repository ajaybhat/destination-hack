from flask import Flask, jsonify, request, g, render_template
from sqlite3 import connect
from contextlib import closing

SCHEMA = 'schema.sql'
DATABASE = 'destination.db'
app = Flask(__name__)

def connect_db():
    return connect(DATABASE)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource(SCHEMA, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

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
    cur = g.db.execute('select * from users')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

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
