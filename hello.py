from flask import Flask

app = Flask(__name__)

@app.route("/")
def Phyu():
    return "Hello World"

@app.route("/Phyu")
def tiide():
    return "Welcome to Phyu Phyu Aye"
