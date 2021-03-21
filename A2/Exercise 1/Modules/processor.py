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

def processing(tweets_path):
    #Create document_word_dict
    document_word_dict = {}
    
    with open(tweets_path, encoding = "utf-8-sig") as file:
        tweets_data = csv.reader(file, delimiter = '\t')
        
        for id, text in tweets_data:

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
            
            for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):
                document_word_dict[int(str(id))] = message_embedding #keeping this structure intact is important
            
    return document_word_dict