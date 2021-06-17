from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/')

def hello_world():

    user = request.values.get("text field") 

    return render_template("index.html",name = user)




if __name__ == '__main__':
    app.run()
