from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/', methods=['POST', 'GET'])
def hello():
    name = request.form['name']
    return render_template('hello.html', name=name)


@app.route('/account/<string:name>')
def account(name):
    return render_template('hello.html', name=name)
