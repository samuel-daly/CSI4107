from collections import Counter
import math
import json
import copy


def do_indexer(document_word_count_dict, document_word_dict):

    #############################
    #frequency_dict
    #This dictionary with frequency values will be used for queries
    
    #Create a list for all words (no duplicates)
    all_words = []

    #Iterate through document_word_dict
    for i in document_word_dict:
        token_words = document_word_dict.get(i)

        #Iterate through token_words
        for word in token_words:
            if word not in all_words:
                all_words.append(word)

    #Create dictionary from array list
    frequency_dict = {}
    for i in all_words:
        frequency_dict[i] = {}

    #Add inner keys to dictionary
    for i in document_word_count_dict:
        doc = document_word_count_dict.get(i)
        for word in doc:
            number = doc.get(word)
            frequency_dict[word][i] = number


    #Test out frequency_dict (can comment out)
    #print(frequency_dict)

    
    #Save to folder
    #Important: When we test later, we only need to load the json file (No need to recreate a new file every query)
    frequency_dict_path = "Modules/data/frequency_dict.json"
    with open(frequency_dict_path, "w") as file:
        json.dump(frequency_dict, file)
    

    #############################
    #weighted_dict
    #This dictionary with weighted values will be used for queries

    #copy frequency_dict to weighted_dict
    weighted_dict = copy.deepcopy(frequency_dict)
    
    #frequency_dict size
    dict_size = len(weighted_dict)
    
    for word in weighted_dict:

        #creates copy of weighted_dict[word]
        documents = weighted_dict[word]
        
        #documents size
        doc_freq = len(documents)
        
        #calculates max_freq
        documents = weighted_dict.get(word,{})
        max_freq = 0
        for i in documents:
            if documents[i] > max_freq:
                max_freq = documents[i]

        #calculate inv_doc_freq
        inv_doc_freq = math.log((float(dict_size) / doc_freq), 2)

        
        for id in documents:

            #creates copy of documents[id]
            freq = documents[id]

            #calculate word_freq
            word_freq = float(freq) / max_freq

            #calculate weight value
            weight = inv_doc_freq * word_freq

            #set weight value to dict
            documents[id] = weight

            
    #Test out weighted_dict (can comment out)
    #print(weighted_dict)

    
    #Save to folder
    #Important: When we test later, we only need to load the json file (No need to recreate a new file every query)
    weighted_dict_path = "Modules/data/weighted_dict.json"
    with open(weighted_dict_path, "w") as file:
        json.dump(weighted_dict, file)
    
    #############################

    #This section below is no longer required
    
    #Returns both dictionaries (frequency_dict) and (weighted_dict)
    #return frequency_dict, weighted_dict

    











