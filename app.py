from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
@app.route("/resister")
def resister():
    return "resister"
@app.route("/search")
def search():
    return "search"
