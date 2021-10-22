from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Worlcocddddddd!</p>"

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")

