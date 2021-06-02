from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')
    
@app.route('/api/<name>')
def hello(name):
    return name




# pip3 install pipenv
# python3 -m pipenv install
# python3 -m pipenv shell
# python3 -m flask run
