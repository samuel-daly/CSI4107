from Modules.preprocessor import do_preprocessor
from Modules.indexer import do_indexer
import re
from xml.etree import ElementTree

#CREATES INDEX VIA JSON FILE

#Paths
stopwords_path = "Modules/data/stopwords.txt"

#I am using a shorter version because the regular one takes too long to test
tweets_path = "Modules/data/trec-microblog11-short.txt"



#Pre-processing
document_word_dict, document_word_count_dict = do_preprocessor(tweets_path, stopwords_path)

#Indexing
do_indexer(document_word_count_dict, document_word_dict)

#TO DO: should return 2 dictionaries
# x_dict, y_dict = do_indexer(document_word_count_dict, document_word_dict)







