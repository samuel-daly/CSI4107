from collections import Counter
import csv
import re
import nltk
from nltk.stem.snowball import EnglishStemmer
import string
from nltk import TreebankWordTokenizer
from xml.etree import ElementTree
from numpy.linalg import linalg
import json
import math
from Modules.Word2Vec.word2vecReader import Word2Vec


def query_processing(text, weighted_dict):

    punct_set = set(string.punctuation)
    
    stopwords_path = "Modules/data/stopwords.txt"
    stopwords = set(line.strip() for line in open(stopwords_path))
    
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

    #Remove stopwords
    for x in words:
        if x in stopwords:
            words.remove(x)
    
    #Remove words that contain numbers
    tmp2 = []
    for x in range(len(words)):
        if bool(re.match(r'\b[a-zA-Z]+\b', words[x])):
            tmp2.append(words[x])
    words = tmp2

    #Remove (u"\u201d) from words
    tmp3 = []
    for x in words:
        tmp3.append(x.replace(u"\u201d", ""))
    words = tmp3

    #Word counter
    word_counter = Counter(words)

    #Intialize both word and frequency vectors
    w_vect = []
    f_vect = []

    #Iterate through all words
    for word in words:
        
        w_vect.append(word)

        #calculate max_freq
        documents = weighted_dict.get(word,{})

        max_freq = 0
        for i in documents:
            if documents[i] > max_freq:
                max_freq = documents[i]

        if(max_freq > 0):
            #calculate inv_doc_freq
            doc_freq = len(documents)
            inv_doc_freq = math.log((float(len(weighted_dict)) / doc_freq), 2)

            for id in documents:

                #creates copy of documents[id]
                freq = documents[id]

                #calculate word_freq
                word_freq = float(freq) / max_freq

                #calculate weight value
                weight = inv_doc_freq * (0.5 + (0.5 * word_freq))

            #append calculated weight value to f_vect
            f_vect.append(weight)
            
        else:
            #append weight value as 0
            f_vect.append(0)

    #Return both (w_vect) and (f_vect)
    return (w_vect, f_vect)

def new_queries(words, weighted_dict):
    #remove punctuations
    punct_set = string.punctuation

    new_words = []

    #Intialize both word and frequency vectors
    w_vect = []
    f_vect = []

    for word in words:
        no_punct = ""
        for char in word:
            if char not in punct_set:
                no_punct = no_punct + char
        new_words.append(no_punct.lower())

    #Iterate through all words
    for word in new_words:
        
        w_vect.append(word)

        #calculate max_freq
        documents = weighted_dict.get(word,{})

        max_freq = 0
        for i in documents:
            if documents[i] > max_freq:
                max_freq = documents[i]

        if(max_freq > 0):
            #calculate inv_doc_freq
            doc_freq = len(documents)
            inv_doc_freq = math.log((float(len(weighted_dict)) / doc_freq), 2)

            for id in documents:

                #creates copy of documents[id]
                freq = documents[id]

                #calculate word_freq
                word_freq = float(freq) / max_freq

                #calculate weight value
                weight = inv_doc_freq * (0.5 + (0.5 * word_freq))

            #append calculated weight value to f_vect
            f_vect.append(weight)
            
        else:
            #append weight value as 0
            f_vect.append(0)

    #Return both (w_vect) and (f_vect)
    return (w_vect, f_vect)        



def do_query(document_word_dict_path, frequency_dict_path, weighted_dict_path, queries_path):

    name = "myRun"

    ###################
    #LOADING FILES

    '''
    #NOT USED (KEEP JUST IN CASE)
    
    #document_word_dict
    document_word_dict = {}
    with open(document_word_dict_path, "rb") as file:
        document_word_dict = json.loads(file.read())

    #frequency_dict
    frequency_dict = {}
    with open(frequency_dict_path, "rb") as file:
        frequency_dict = json.loads(file.read())
    '''
        
    #weighted_dict
    weighted_dict = {}
    with open(weighted_dict_path, "rb") as file:
        weighted_dict = json.loads(file.read())
    
    ###################


    #Initialize xml tree
    t = ElementTree.parse(queries_path)

    # Loading the Word2Vec Model
    model_path = "Modules/Word2Vec/word2vec_twitter_model.bin"
    print("--- Loading the word2vec model, this will take some time ----")
    model = Word2Vec.load_word2vec_format(model_path, binary=True)
    print("The vocabulary size is: "+str(len(model.vocab)))

    # To find synonyms for words in query
    # ex:   similar = model.most_similar('healthcare')
    #       words = list((w[0] for w in similar))
    #       words -> will give the synonyms for said word, in this case healthcare

    #Create Results
    with open("Modules/data/results_new.txt", 'w') as file:
        for q in t.getroot():

            #Sets Query ID
            #query_id = q[0].text[9:][:-1] #string value (MB001)
            query_id = q[0].text
            query_id = re.sub('[^0-9]','', query_id) #only digits remain
            query_id = query_id.lstrip('0') #removes zeros and strings

            
            #Query Processing
            w_vect, f_vect = query_processing(q[1].text, weighted_dict)

            print("Old Word Vector -- " + str(w_vect))

            # New word vect
            temp_w_vect = []
        
            # Go through w_vect and add synonyms for each word in the query
            for word in w_vect:
                try:    
                    similar = model.most_similar(word)
                    words_similar = list(w[0] for w in similar)
                    temp_w_vect.append(word)
                    for i in range(2):
                        temp_w_vect.append(words_similar[i])
                except:
                    temp_w_vect.append(word)
                    continue

            
            # Replace w_vect with the new vect
            new_w_vect, new_f_vect = new_queries(temp_w_vect, weighted_dict)
            w_vect = new_w_vect
            f_vect = new_f_vect

            print("New Word Vector -- " + str(w_vect))
            print("Frequency Vector -- " + str(f_vect))

            print("----------- Next query -------------")


            #Create unique set of documents associated to each word in w_vect
            unique_set_of_documents = set()

            #iterate though w_vect for every word
            for word in w_vect:

                #iterate through keys in weighted_dict
                for d in weighted_dict.get(word,{}).keys():
                    unique_set_of_documents.add(d)

            
            #Create vector frequency document for query
            document_vect = {}
            for doc_id in unique_set_of_documents:
                document_vect[doc_id] = []

            #Initialize counter to 0
            counter = 0

            #iterate though w_vect for every word
            for word in w_vect:

                #iterate through unique_set_of_documents
                for d in unique_set_of_documents:
                    document_vect[d].insert(counter, weighted_dict.get(word,{}).get(d,0))

                #Add +1 to counter
                counter = counter + 1 #works better than ++counter (better results)


            #Create document ranking array for all documents
            document_ranking = []

            #Iterate though document_vect for every id
            for id in document_vect:

                #Calculate cos similarity value
                value = linalg.dot(document_vect[id], f_vect) / (linalg.norm(document_vect[id]) * linalg.norm(f_vect))

                #Append value and id to document_ranking
                document_ranking.append({"id":id, "value": value})

            #Sort documents by highest value first
            sorted_ranking = sorted(document_ranking, key=lambda d:d["value"], reverse=True)

            #for every relevant document in query
            for d in range(len(sorted_ranking)):
                
                #Writes line info to txt file
                file.write(query_id + " " + "Q0 " + str(sorted_ranking[d].get("id")) + " " + str(d + 1) + " " + str(sorted_ranking[d].get("value")) + " " + name + "\n")

                #stops for loop at 1000th document
                if d == 999:
                    break
            







