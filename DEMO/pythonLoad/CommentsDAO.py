import mysql.connector
from RawComment import *

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="KRPCGroup",
    database="isss609gp06"
)

class CommentsDAO:
    def InsertComment(rawComment:RawComment):
        database.commit()
        cursor=database.cursor()

        #try:
        sql="insert into main (RID,rating,yearMonth,reviewerLocation,reviewText,branch,dominantTopic,featureName,sentiment) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(rawComment.RID,rawComment.rating,rawComment.getYearMonthInQueryFormat(),rawComment.reviewerLocation,rawComment.reviewText,rawComment.branch,rawComment.dominantTopic,rawComment.featureName,rawComment.sentiment)
        cursor.execute(sql,val)
        database.commit()
        #except:
        print("EXCEPT IN InsertComment")