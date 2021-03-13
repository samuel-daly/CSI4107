from Modules.query import do_query

#TESTS QUERIES

#Paths
document_word_dict_path = "Modules/data/document_word_dict.json"
frequency_dict_path = "Modules/data/frequency_dict.json"
weighted_dict_path = "Modules/data/weighted_dict.json"

queries_path = "Modules/data/topics_MB1-49.xml" #All 49 queries
#queries_path = "Modules/data/topics_MB1-49-one.xml" #1 query


#Query
do_query(document_word_dict_path, frequency_dict_path, weighted_dict_path, queries_path)











