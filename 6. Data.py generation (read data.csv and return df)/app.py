
'''
Created on 
    

Course work: 18-05-2021
    

@author: 
    Ana Jessica

Source:
    
'''

from flask import Flask,render_template, jsonify, request
import json
import species


app  = Flask(__name__)
PORT = 3000

'''
http://0.0.0.0:3000/
'''

@app.route("/", methods=["GET","POST"])
def startpy():

    # return jsonify(result)
    return render_template("index.html") 



if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)
