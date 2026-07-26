# Explore `Flask` module and create a web server using flask and python.4

from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"

app.run()

# python -m pip install flask