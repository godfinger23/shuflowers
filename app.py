from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/one.html")
def one():
    return render_template("one.html")

@app.route("/fulllove.html")
def fulllove():
    return render_template("fulllove.html")

@app.route("/onlyu.html")
def onlyu():
    return render_template("onlyu.html")

@app.route("/all4u.html")
def all4u():
    return render_template("all4u.html")

@app.route("/index.html")
def index1():
    return render_template("index.html")