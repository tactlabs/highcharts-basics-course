from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():

   
    return "Welcome all to Tactlabs"

if __name__ =='__main__': 
    app.run(debug = True) 
