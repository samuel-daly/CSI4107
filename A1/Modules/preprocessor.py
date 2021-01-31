from collections import Counter
import csv
import re
import nltk
from nltk.stem.snowball import EnglishStemmer
import string
from nltk import TreebankWordTokenizer


def do_preprocessor(tweets_path, stopwords_path):

    #Create string punctuation set
    punct_set = set(string.punctuation)
    
    #Create stopwords array from path
    stopwords = set(line.strip() for line in open(stopwords_path))
    
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
                if i.lower() not in stopwords and i.lower() not in punct_set:
                    try:
                        words.append(EnglishStemmer().stem(i.lower()))
                    except:
                        words.append(i.lower())

            #Remove punctuation
            table = str.maketrans('', '', string.punctuation)
            tmp1 = words
            words = [w.translate(table) for w in tmp1]

            #############################
            #Add More Pre-Processing Here

            #- remove ( " )for example: ->>>> 'team”': {35029412940353536: 1}  team" is a word
            


            #############################
    
            
            document_word_dict[int(str(id))] = words #keeping this structure intact is important
            
    
    #Create a temporary dict for (document_word_dict)
    tmp_dict = document_word_dict
    #print(tmp_dict)
    

    #Create document_word_count_dict
    document_word_count_dict = {}
    for doc in tmp_dict:
        document_word_count_dict[doc] = Counter(tmp_dict[doc]);
    #print(document_word_count_dict)


    #Returns both dictionaries (document_word_dict) and (document_word_count_dict)
    return document_word_dict, document_word_count_dict
    








