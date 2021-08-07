import os, requests
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
    	return render_template("index.html")
    else:
    	return render_template("index.html")

@app.route("/one", methods=["GET", "POST"])
def one():
    if request.method == "POST":
    	return render_template("one.html")
    else:
    	return render_template("one.html")

@app.route("/fulllove", methods=["GET", "POST"])
def fulllove():
    if request.method == "POST":
    	return render_template("fulllove.html")
    else:
    	return render_template("fulllove.html")

@app.route("/onlyu", methods=["GET", "POST"])
def onlyu():
    if request.method == "POST":
    	return render_template("onlyu.html")
    else:
    	return render_template("onlyu.html")

@app.route("/all4u", methods=["GET", "POST"])
def all4u():
    if request.method == "POST":
    	return render_template("all4u.html")
    else:
    	return render_template("all4u.html")
