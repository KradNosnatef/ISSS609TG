import csv
from RawComment import *
from CommentsDAO import *
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import json

country={}
dictionary={}
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

        dictionary[str(rows[i][0])]=stemmedComment
        print(i)

    fileSaved=open("./assets/processedComments.txt","w",encoding="utf-8")
    fileSaved.write(json.dumps(dictionary))
    fileSaved.close()
