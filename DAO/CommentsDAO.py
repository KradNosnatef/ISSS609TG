import mysql.connector
from RawComment import *

database=mysql.connector.connect(
    host="192.168.50.70",
    user="fuqianshan",
    passwd="KRPCGroup",
    database="isss609gp06"
)

cursor=database.cursor()

class CommentsDAO:
    def InsertComment(rawComment):
        BID=CommentsDAO.SearchAndInsertBranch(rawComment.branch)
        LID=CommentsDAO.SearchAndInsertReviewrLocation(rawComment.reviewerLocation)
        
        try:
            sql="update comments SET Rating=%s,YearMonth=%s,LID=%s,BID=%s WHERE RID=%s;"
            val=(rawComment.rating,rawComment.getYearMonthInQueryFormat(),LID,BID,rawComment.RID)
            #print(val)
            cursor.execute(sql,val)
            database.commit()
        except:
            print("?")
            pass


    def SearchAndInsertBranch(branch):
        sql="select * from branch where BranchName=%s;"
        cursor.execute(sql,(branch,))
        result=cursor.fetchall()
        
        if len(result)==0:
            sql="insert into branch (BranchName) values (%s);"
            cursor.execute(sql,(branch,))
            database.commit()

        sql="select BID from branch where BranchName=%s;"
        cursor.execute(sql,(branch,))
        result=cursor.fetchall()
        return(int(result[0][0]))
        

    def SearchAndInsertReviewrLocation(reviewerLocation):
        sql="select * from reviewerLocation where LocationName=%s;"
        cursor.execute(sql,(reviewerLocation,))
        result=cursor.fetchall()
        
        if len(result)==0:
            sql="insert into reviewerLocation (LocationName) values (%s);"
            cursor.execute(sql,(reviewerLocation,))
            database.commit()

        sql="select LID from reviewerLocation where LocationName=%s;"
        cursor.execute(sql,(reviewerLocation,))
        result=cursor.fetchall()
        return(int(result[0][0]))