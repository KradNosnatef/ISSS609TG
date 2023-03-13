import csv

with open("./assets/DisneylandReviews.csv","r",encoding="ISO-8859-1") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

