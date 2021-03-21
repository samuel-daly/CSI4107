import embed
from Modules.processor import processing
from Modules.query import create_results

# Paths
tweets_path = "Modules/data/trec-microblog11.txt"
queries_path = "Modules/data/topics_MB1-49.xml"

# First step, process the tweets
tweets_embeddings = processing(tweets_path)

# Create the results
create_results(tweets_embeddings, queries_path)


