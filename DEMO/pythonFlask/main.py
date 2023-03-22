from flask import Flask
from flask import request
from flask_cors import *
from CommentsDAO import *
import requests
import json

app=Flask(__name__)
@app.route("/cmd/HelloWorld")
def HelloWorld():
    return("Hello World!")

@app.route("/cmd/getAllComments")
def getAllComments():
    print("call: getAllComments")
    return(json.dumps(CommentsDAO.getAllComments()))

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=25565)