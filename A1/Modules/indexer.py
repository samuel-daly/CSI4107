from collections import Counter
import math
import json #may need to use this later if we need to save files


def do_indexer(document_word_count_dict, document_word_dict):

    #############################
    #frequency_dict
    
    #Create a list for all words (no duplicates)
    all_words = []
    for token in document_word_dict:
        token_words = document_word_dict.get(token)
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
    print(frequency_dict)

    #Save to folder
    frequency_dict_path = "Modules/data/frequency_dict.json"
    with open(frequency_dict_path, "w") as file:
        json.dump(frequency_dict, file)


    #############################
    #weighted_dict
    #This dictionary with weighted values will be used for queries
    #We will create a query.py file once this is complete





    #Save to folder
    #Important: When we test later, we only need to load the json file (No need to recreate a new file every query)
    '''
    weighted_dict_path = "Modules/data/weighted_dict.json"
    with open(weighted_dict_path, "w") as file:
        json.dump(weighted_dict, file)
    '''
        
    #############################

    #Returns both dictionaries (frequency_dict) and (weighted_dict)
    #return frequency_dict, weighted_dict

    











