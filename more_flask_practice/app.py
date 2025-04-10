from flask import Flask


app = Flask(__name__)  #Creating the app instance

@app.route('/')
def home():
    return '<h1>MUSIIMENTA AGNES</h1>'