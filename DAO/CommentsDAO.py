import mysql.connector

database=mysql.connector.connect(
    host="fuqianshan.asuscomm.com",
    user="fuqianshan",
    passwd="KRPCGroup",
    database="isss609gp06"
)

class CommentsDAO:
    def InsertComment(rawComment):
        pass