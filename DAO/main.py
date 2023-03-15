import csv
from RawComment import *
from CommentsDAO import *

country={}
i=0

with open("./assets/DisneylandReviews.csv","r",encoding="ISO-8859-1") as file:
    reader=csv.reader(file)
    rows=[row for row in reader]
    for row in rows[1:]:
        print(str(i)+"/50000")
        i=i+1
        rawComment=RawComment(row)
        CommentsDAO.InsertComment(rawComment)
        #print(rawComment.getYearMonthInQueryFormat())
