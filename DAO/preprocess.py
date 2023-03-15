import csv
from RawComment import *
from CommentsDAO import *
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import json

country={}
i=0

with open("./assets/DisneylandReviews.csv","r",encoding="ISO-8859-1") as file:
    reader=csv.reader(file)
    rows=[row for row in reader]
    rows=rows[1:]

    comments=[row[4] for row in rows]
    for i in range(0,len(rows)):
        comment=rows[i][4]
        tokenizedComment=[word.lower() for word in nltk.word_tokenize(comment) if word not in string.punctuation]
        
        stopWordsRemovedComment=[word for word in tokenizedComment if word not in stopwords.words("english")]
        
        stemmer=PorterStemmer()

        stemmedComment=[stemmer.stem(word) for word in stopWordsRemovedComment]
        #print(stemmedComment)

        fileSaved=open("./assets/processedComments/"+str(rows[i][0])+".txt","w",encoding="utf-8")
        fileSaved.write(json.dumps(stemmedComment))
        fileSaved.close()
        print(i)

