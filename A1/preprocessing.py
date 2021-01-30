import nltk
import re
import string


# Step 1: Open file and read it
tweets = open('tweets.txt', 'r')
tweets_read = tweets.read()

# Step 2: Remove links
no_links = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", tweets_read)

# Step 3: Split the file
tweets_words = no_links.split()

# Step 4: Remove punctuations
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tweets_words]

# Step 5: Remove all numbers
no_numbers = [token for token in stripped if not token.isdigit()]

# Step 6 - Remove words that contain numbers
regex = []
for x in range(len(no_numbers)):
    if bool(re.match(r'\b[a-zA-Z]+\b', no_numbers[x])):
        regex.append(no_numbers[x])

for x in range(len(regex)):
    regex[x] = regex[x].lower()

# Step 7 - Remove the stopwords
stopwords = open('stopwords.txt', 'r')
stopwords_list = stopwords.read().split()


# WHAT WE NEED TO FILTER OUT
# 
# 1. Punctuation
# 2. Numbers
# 3. links
# 4. Stopwords
# 5. 



# # Replace all the \t with a space
# tweets_read = tweets_read.replace('\t', ' ')

# # Split all the lines to separate the tweets
# # tweets_read = tweets_read.splitlines()

# # Time to remove all the punctuations
# tweets_words = tweets_read.split()

# lower_words = [word.lower() for word in stripped]
# # print(lower_words)
# no_numbers = [token for token in lower_words if not token.isdigit()]
# print(no_numbers)

# Step 3 - Remove all stop words

# Step 4 - Stem the words 

