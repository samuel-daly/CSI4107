# Assignment 1 - CSI4107

## Students
Samuel Daly - 8173488  
Ryan Matte - 300027432  
Michel Moore - 300063096

## Task Division
Step 1: Samuel Daly  
Step 2: Michel Moore  
Step 3: Ryan Matte  
Step 4: Ryan Matte  
Step 5: Samuel Daly  

## Folder Layout

```
├── Modules
│   ├── data
│   │   ├── document_word_dict.json
│   │   ├── frequency_dict.json
│   │   ├── stopwords.txt
│   │   ├── topics_MB1-49.xml
│   │   ├── trec-microblog11-qrels.txt
│   │   ├── trec-microblog11.txt
│   │   └── weighted_dict.json
│   ├── indexer.py
│   ├── preprocessor.py
│   └── query.py
├── requirements.txt
├── create_index.py
└── create_results.py
```

## How to run the program

First we need to install some packages. Run ***pip install -r requirements.txt*** if you're on windows, and if you're on MacOS run ***pip3 install -r requirements.txt***  
To create the inverted index, run ***python create_index.py*** if you're on windows, and if you're on MacOS run ***python3 create_index.py***
Next, to create the results, run ***python create_results.py*** if you're on windows, and if you're on MacOS run ***python3 create_results.py***

## Functionality of the program

For this assignment, we had to work in order of steps. The first step was to pre-process all of the tweets. All of the preprocessing for the tweets is done in the **processor.py** file. We created a function that takes the file path for the tweets and the file path for the stopwords. In this function we start off by reading the file of tweets and the goal is to process them to create a vocabulary that we will use to create the inverted index and then use for the future steps. We initially remove the links since we do not want those in the vocabulary. Next, we stem the words to create a better vocabulary. To do this we use the *English Stemmer* from the NLTK library. This simplified the stemming for us. Next steps were to remove the punctuation, the stopwords and all the words that also contained numbers in them. We realized that the punctuation removal was leaving some weird unicode text behind, so we added more processing to get rid of those. This process was done for each tweet and therefore created a dictionary for each tweet that contained the tokenized, stemmed and processed words. The data structure used for this step is a dictionary which allows us to keep a list of words for each tweet id. It makes it easy to access in the future and it is very maintainable. This dictionary was saved under the file *document_word_dict.json* which we then use to do the indexing in the future steps.

Once the processing was done for each tweet and it was saved in a dictionary for us to refer, we went ahead and built the inverted index.

# Indexing
write here

# Retrieval and ranking
write here

# Results

With everything done and working, we went ahead and ran the **trec_eval script** to test our results with the qrels file that we were supplied with. To run the script, we used this command: *./trec_eval -m map -m P.10 trec_microblog11-qrels.txt results.txt*
After running for the MAP (Mean Average Precision and the P10 (Precision in the first 10 documents retrieved), these were our results:

```
map                   	all	0.2771
P_10                  	all	0.3020
```



## Sample tokens from the vocabulary

Vocabulary size = 53310 words

ottawa  
human  
societi  
adopt  
chicacuppacupp  
matter  
rich  
poor  
life  
money  
call  
refundcheck  
name  
class  
oceanographi  
multimedia  
techniques  
tvd  
death  
burnley  
teen  
controversi  
control  
contribut  
dec  
express  
hurt  
lol  
woof  
vintag  
red  
leather  
sailor  
nautic  
jojoluvsjon  
cesarmillan  
savelennox  
calm  
influenc  
comendo  
cama  
euri  
nowplay  
fear  
ghost  
pig  
dont  
minut  
analys  
chandeli  
primeiro  
ofici  
novo  
millan  
hora  
renata  
peixoto  
pedro  
glad  
enjoy  
stuff  
junebug  
glori  
snowdog  
god  
son  
ya  
rid  
sooni  
help  
dude  
worry  
ella  
pretti  
green  
nice  
cuddl  
buddi  
handmad  
esti  
post  
labrador  
retriev  
adult  
eukanuba  
food  
gent  
tenho  
que  
consola  
prima  
aqui  
pq  
sabe  
mando  
resposta  
dizendo  
se  
era  
naum  

## Sample queries

### Query 3

Query 3: "Haiti Aristide return"

#### Results

1. 32384227123134464
2. 32211683082502144
3. 29296574815272960
4. 32411439918489600
5. 32387196078006272
6. 29613127372898304
7. 32080564265680898
8. 31034174752169984
9. 33711164877701120
10. 34694060157435904

### Query 20


