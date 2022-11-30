from flask import Flask,request,url_for,redirect,render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")