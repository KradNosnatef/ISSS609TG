import csv
from RawComment import *
from CommentsDAO import *

country={}

with open("./assets/DisneylandReviews.csv","r",encoding="ISO-8859-1") as file:
    reader=csv.reader(file)
    rows=[row for row in reader]
    for row in rows[1:]:
        rawComment=RawComment(row)
        CommentsDAO.InsertComment(rawComment)
