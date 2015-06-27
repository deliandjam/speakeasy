from flask import Flask, request, url_for
from flask import render_template
from index import *
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/create', methods = ['POST'])
def create_url():
    name = request.form['name']

    success = create_radio(name)
    key = success[0][unicode('success')][unicode('objectId')]
    return json.dumps({'success': True, 'id': key}, 200, {'ContentType': 'application/json'})

@app.route('/radio/<radio_id>')
def show_radio(radio_id):
    return render_template('user.html')

@app.route('/radio/<radio_id>/play', methods = ['POST'])
def play(radio_id):
    success = get_top_request(radio_id)
    url = success[unicode('url')]
    return json.dumps({'success': True, 'url': url}, 200, {'ContentType': 'application/json'})

@app.

if __name__ == '__main__':
    app.run()
