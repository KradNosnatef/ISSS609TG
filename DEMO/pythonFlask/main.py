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

@app.route("/cmd/getCommentsWithFilter",methods=['POST'])
@cross_origin()
def getCommentsWithFilter():
    print(request.data.decode())

    jsonObject=json.loads(request.data.decode())

    #return "yeah"
    return json.dumps(CommentsDAO.getCommentsWithFilter(jsonObject["returnNumberLimit"],jsonObject["rating"],jsonObject["monthNotLastThan"],jsonObject["reviewerLocation"],jsonObject["branch"],jsonObject["dominantTopic"],jsonObject["sentiment"],jsonObject["orderBy"],jsonObject["DESCorASC"]))

@app.route("/cmd/getPossibleReviewerLocation")
def getPossibleReviewerLocation():
    print(CommentsDAO.getPossibleReviewerLocation())
    return(json.dumps(CommentsDAO.getPossibleReviewerLocation()))