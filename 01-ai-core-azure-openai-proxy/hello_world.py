from flask import Flask

app = Flask(__name__)

@app.route('/teste', methods=['POST'])
def hello_world():
    return "<p>Hello, World!</p>"