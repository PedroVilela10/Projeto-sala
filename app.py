from flask import Flask, render_template, request, redirect, url_for, session

import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return render_template('index.html')