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
    return json.dumps(CommentsDAO.getCommentsWithFilter(jsonObject["returnNumberLimit"],jsonObject["rating"],jsonObject["monthNotLastThan"],jsonObject["reviewerLocation"],jsonObject["branch"],jsonObject["dominantTopic"],jsonObject["sentiment"],jsonObject["orderBy"],jsonObject["DESCorASC"],jsonObject["page"]))

@app.route("/cmd/getCommentsNumberGroupByYearMonthWithFilter",methods=['POST'])
@cross_origin()
def getCommentsNumberGroupByYearMonthWithFilter():
    print(request.data.decode())

    jsonObject=json.loads(request.data.decode())
    queryResult=CommentsDAO.getCommentsNumberGroupByYearMonthWithFilter(jsonObject["rating"],jsonObject["monthNotLastThan"],jsonObject["reviewerLocation"],jsonObject["branch"],jsonObject["sentiment"])
    queryResultAsDict={}
    for row in queryResult:
        queryResultAsDict[str(row[0])]=row[1]
    result={
        "xName":[],
        "yValue":[]
    }
    if jsonObject["monthNotLastThan"]==None:monthNotLastThan=120
    else: monthNotLastThan=jsonObject["monthNotLastThan"]
    for i in range(0,monthNotLastThan+1):
        result["xName"].append(str(i))
        if str(i) in queryResultAsDict:result["yValue"].append(queryResultAsDict[str(i)])
        else: result["yValue"].append(0)

    return json.dumps(result)



@app.route("/cmd/getPossibleReviewerLocation")
def getPossibleReviewerLocation():
    print(CommentsDAO.getPossibleReviewerLocation())
    return(json.dumps(CommentsDAO.getPossibleReviewerLocation()))