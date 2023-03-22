import csv
from RawComment import *
from CommentsDAO import *

with open("./DEMO/pythonLoad/sample_demo_data.CSV","r",encoding="ISO-8859-1") as file:
    reader=csv.reader(file)
    rows=[row for row in reader]
    for row in rows[1:]:
        print(row)
        rawComment=RawComment(row)
        CommentsDAO.InsertComment(rawComment)
