import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="KRPCGroup",
    database="isss609gp06"
)

class CommentsDAO:
    def reconnect():
        global database

        database=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="KRPCGroup",
            database="isss609gp06"
        )


    def getAllComments():
        database.commit()
        cursor=database.cursor()
        sql="select RID,rating,cast(DATE_Format(yearMonth,'%Y-%m') as char(20)),reviewerLocation,reviewText,branch,dominantTopic,featureName,sentiment from main;"
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        return(result)
    
    def getCommentsWithFilter(returnNumberLimit:int=8,rating:int or None=None,monthNotLastThan:int or None=None,reviewerLocation:str or None=None,branch:str or None=None,dominantTopic:int or None=None,sentiment:str or None=None,orderBy:str="yearMonth",DESCorASC:str="DESC",page:int=0):
        sql="select RID,rating,cast(DATE_Format(yearMonth,'%Y-%m') as char(20)),reviewerLocation,reviewText,branch,dominantTopic,featureName,sentiment from main"
        where=" where"
        clause=""
        val=()

        if rating!=None:
            clause=clause+" rating=%s and"
            val=val+(rating,)

        if monthNotLastThan!=None:
            clause=clause+" TIMESTAMPDIFF(MONTH,yearMonth,NOW())<=%s and"
            val=val+(monthNotLastThan,)

        if reviewerLocation!=None:
            clause=clause+" reviewerLocation=%s and"
            val=val+(reviewerLocation,)

        if branch!=None:
            clause=clause+" branch=%s and"
            val=val+(branch,)

        if dominantTopic!=None:
            clause=clause+" dominantTopic=%s and"
            val=val+(dominantTopic,)

        if sentiment!=None:
            clause=clause+" sentiment=%s and"
            val=val+(sentiment,)

        if clause!="":
            clause=clause.rstrip("dna")
            sql=sql+where+clause

        sql=sql+" ORDER BY "+orderBy+" "+DESCorASC+" LIMIT %s,%s;"
        val=val+(page*returnNumberLimit,returnNumberLimit,)

        print(sql)
        try:
            database.commit()
            cursor=database.cursor()
            cursor.execute(sql,val)
            result=cursor.fetchall()
            cursor.close()
            return result
        except:
            CommentsDAO.reconnect()
            print("except in getCommentsWithFilter")
            return CommentsDAO.getCommentsWithFilter(returnNumberLimit,rating,monthNotLastThan,reviewerLocation,branch,dominantTopic,sentiment,orderBy,DESCorASC)
        
    def getCommentsNumberGroupByYearMonthWithFilter(rating:int or None=None,monthNotLastThan:int or None=None,reviewerLocation:str or None=None,branch:str or None=None,sentiment:str or None=None):
        sql="select TIMESTAMPDIFF(MONTH,yearMonth,NOW()),count(TB.yearMonth) from (select * from main"
        where=" where"
        clause=""
        val=()

        if rating!=None:
            clause=clause+" rating=%s and"
            val=val+(rating,)

        if monthNotLastThan!=None:
            clause=clause+" TIMESTAMPDIFF(MONTH,yearMonth,NOW())<=%s and"
            val=val+(monthNotLastThan,)

        if reviewerLocation!=None:
            clause=clause+" reviewerLocation=%s and"
            val=val+(reviewerLocation,)

        if branch!=None:
            clause=clause+" branch=%s and"
            val=val+(branch,)

        if sentiment!=None:
            clause=clause+" sentiment=%s and"
            val=val+(sentiment,)

        if clause!="":
            clause=clause.rstrip("dna")
            sql=sql+where+clause

        sql=sql+") as TB GROUP BY TB.yearMonth;"
        print(sql)

        database.commit()
        cursor=database.cursor()
        cursor.execute(sql,val)
        result=cursor.fetchall()
        cursor.close()
        return result



    def getPossibleReviewerLocation():
        sql="select reviewerLocation from main group by reviewerLocation;"

        try:
            database.commit()
            cursor=database.cursor()
            cursor.execute(sql)
            result=cursor.fetchall()
            for i in range(0,len(result)):
                result[i]=result[i][0]
            cursor.close()
            return result
        except:
            CommentsDAO.reconnect()
            print("except in getPossibleReviewerLocation")
            return CommentsDAO.getPossibleReviewerLocation()
        
#print(CommentsDAO.getCommentsNumberGroupByYearMonthWithFilter())