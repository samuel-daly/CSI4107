from collections import Counter
import csv
import re
import nltk
from nltk.stem.snowball import EnglishStemmer
import string
from nltk import TreebankWordTokenizer
import json
from embed import embed
import numpy as np
import tensorflow_hub as hub
from xml.etree import ElementTree
from numpy.linalg import linalg
import math

def do_query(text):
    #Remove links
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"https\S+", "", text)
    text = re.sub(r"www\S+", "", text)

    #Initialize words array
    words = []

    for i in TreebankWordTokenizer().tokenize(text):
        words.append(i)

    # Remove words that contain numbers
    tmp2 = []
    for x in range(len(words)):
        if bool(re.match(r'\b[a-zA-Z]+\b', words[x])):
            tmp2.append(words[x])
    words = tmp2

    #Add More Pre-Processing Here
    tmp3 = []
    for x in words:
        tmp3.append(x.replace(u"\u201d", ""))
    words = tmp3

    words_to_string = " ".join([str(elem) for elem in words])

    message_embeddings = embed([words_to_string])

    query_embeddings = []

    for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
        query_embeddings = message_embedding

    return query_embeddings


def create_results(tweets_embeddings, queries_path):

    name = "myRun"

     #Initialize xml tree
    t = ElementTree.parse(queries_path)

    #Create Results
    with open("Modules/data/results.txt", 'w') as file:
        for q in t.getroot():

            #Sets Query ID
            #query_id = q[0].text[9:][:-1] #string value (MB001)
            query_id = q[0].text
            query_id = re.sub('[^0-9]','', query_id) #only digits remain
            query_id = query_id.lstrip('0') #removes zeros and strings

            queries_embeddings = do_query(q[1].text)

            document_ranking = []

            for key, value in tweets_embeddings.items():
                corr = np.inner(queries_embeddings, value)
                document_ranking.append({"id":key, "value": corr})

            sorted_ranking = sorted(document_ranking, key=lambda d:d["value"], reverse=True)

            #for every relevant document in query
            for d in range(len(sorted_ranking)):
                
                #Writes line info to txt file
                file.write(query_id + " " + "Q0 " + str(sorted_ranking[d].get("id")) + " " + str(d + 1) + " " + str(sorted_ranking[d].get("value")) + " " + name + "\n")

                #stops for loop at 1000th document
                if d == 999:
                    break


