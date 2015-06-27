from flask import Flask
app = Flask(__name__)

@app.route('/')
def create_radio():
    return 'Hay this works'


if __name__ == '__main__':
    app.run()