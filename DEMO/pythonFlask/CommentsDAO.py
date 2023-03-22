import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="KRPCGroup",
    database="isss609gp06"
)

class CommentsDAO:
    def getAllComments():
        database.commit()
        cursor=database.cursor()
        sql="select RID,rating,cast(yearMonth as char(20)),reviewerLocation,reviewText,branch,dominantTopic,featureName,sentiment from main;"
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        return(result)
    
#print(CommentsDAO.getAllComments())
        