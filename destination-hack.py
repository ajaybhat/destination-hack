from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/destihack/putuser', methods=['POST'])
def put():
    json_string = request.get_json(force=True)
    print json_string
    return ''   


@app.route('/destihack/newuser')
def newuser():
    user = {'name': 'Ajay', 'surname': 'Bhat', 'age': '22'}
    return jsonify(user)


@app.route('/destihack/')
@app.route('/destihack/index')
def index():
    return 'Hi. Destihack webapp aanu ithu'

@app.route('/')
def xx():
    return 'Hi'

if __name__ == '__main__':
    app.run()
