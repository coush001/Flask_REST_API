from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')



@app.route('/hello', methods=['POST'])
def hello():
    print('request for hello page recieved')
    return render_template('hello.html')
