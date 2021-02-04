# Assignment 1 - CSI4107

### Students
Samuel Daly - 8173488  
Ryan Matte -  
Michel Moore -  

### Task Division
Step 1: Samuel Daly  
Step 2: Michel Moore  
Step 3: Ryan Matte  
Step 4: Ryan Matte  
Step 5: Samuel Daly  

### Folder Layout

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

### How to run program

First we need to install some packages. Run ***pip install -r requirements.txt*** if you're on windows, and if you're on MacOS run ***pip3 install -r requirements.txt***  
To create the inverted index, run ***python create_index.py*** if you're on windows, and if you're on MacOS run ***python3 create_index.py***
Next, to create the results, run ***python create_results.py*** if you're on windows, and if you're on MacOS run ***python3 create_results.py***

### Functionality of the program

For this assignment, we had to work in order of steps. The first step was to pre-process all of the tweets.All of the preprocessing for the tweets is done in the **processor.py** file. We created a function that takes the file path for the tweetsand the file path for the stopwords. In this function we start off by reading the file of tweets and the goal is to process them to create a vocabulary that we will use to create the inverted index and then use for the future steps. We initially remove the links since we do not want those in the vocabulary. Next we stem the words to create a better vocabulary. To do this we using the *English Stemmer* from the NLTK library. This simplified the stemming for us. Next steps were to remove the punctuation, the stopwords and all the words that also contained numbers in them.We realized that the puntuation removal was leaving some weird unicode text behind, so we added more processing to get rid of those. This process was done for each tweet and therefore created a dictionnary for each tweet that contained the tokenized, stemmed and processed words. This dictionnary was saved under the file *document_word_dict.json* which we then use to do the indexing in the future steps.



### Tokens from the vocabulary

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
