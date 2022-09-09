from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template, request, redirect

application = Flask(__name__)

@application.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')



@application.route('/hello', methods=['GET'])
def hello():
    print('request for hello page recieved')
    return render_template('hello.html')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()