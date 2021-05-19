 # -*- coding: utf-8 -*-


#import flask
from flask import Flask
from lib import get_name
app = Flask(__name__)
@app.route("/")



def example():
    name = get_name()
    print(name)
    return "Let's learn Docker!"#add our message


if __name__ == "__main__":
    example()
    #app.run(host="0.0.0.0", port=int("5000"), debug=True)#map port to 5000

#check the localhost to view the app/message

