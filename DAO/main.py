import csv
import mysql.connector

country={}

with open("./assets/DisneylandReviews.csv","r",encoding="ISO-8859-1") as file:
    reader=csv.reader(file)
    for row in reader:



