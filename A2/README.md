# Assignment 2 - CSI4107

## Students
Samuel Daly - 8173488  
Ryan Matte - 300027432  
Michel Moore - 300063096

## Task Division
 

## Folder Layout

### Experiment 1

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
│   ├── word2Vec
│   │   ├── word2vec_twitter_model.bin (Not included in folder since file is too big)
│   │   ├── word2vecReader.py
│   │   └── word2vecReaderUtils.py
│   ├── indexer.py
│   ├── preprocessor.py
│   └── query.py
├── requirements.txt
├── create_index.py
└── create_results.py
```

### Experiment 2

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

### topics_MB1-49.txt must be converted to XML

1. Rename topics_MB1-49.txt to topics_MB1-49.xml
2. Add to first line: `<data>`
3. Add to last line: `</data>`

### Windows

1. To install necessary packages, run ***pip install -r requirements.txt***
2. To create the inverted index, run ***python create_index.py***
3. To create the results, run ***python create_results.py***

### MacOS

1. To install necessary packages, run ***pip3 install -r requirements.txt***
2. To create the inverted index, run ***python3 create_index.py***
3. To create the results, run ***python3 create_results.py***

## Functionality of the program

For this assignment, we had to work in order of steps. The first step was to pre-process all of the tweets. The second step was to build the inverted index and produce a modified weighted dictionary using the modified tf-idf weighting scheme *w_iq = (0.5 + 0.5 tf_iq)∙idf_i*. The third step was to rank the documents in decreasing order of similarity scores using the cosine method. Finally, upon running ***create_results.py***, the program called to ***query.py*** to perform document ranking for every given query in ***topics_MB1-49.xml*** and saved the results in ***results.txt***.


### Future changes
Currently, a problem is that part of our preprocessing code can be found in 2 separate Python files (***preprocessor.py*** and ***query.py***). This means we have some duplicate code. In the future, we plan on storing this function in one place, and having both locations call to this one function. That way, future changes to our preprocessing would only require modification in one location.

## Results

***Add stuff here for the new results of the experiment***

It is important to note that ***create_results.py*** creates different ***results.txt*** files every time it runs. Documents with identical scores are interchangeable. 

For example, in query 1, the first 2 ranked documents are interchangeable:

#### Option 1:
```
1 Q0 30260724248870912 1 0.9944520157716682 myRun
1 Q0 30275282464153600 2 0.9944520157716682 myRun
```

#### Option 2:
```
1 Q0 30275282464153600 1 0.9944520157716682 myRun
1 Q0 30260724248870912 2 0.9944520157716682 myRun
```

Since both scores are identical, their ranks are interchangeable. Therefore, document 30260724248870912 is rank 1 and document 30275282464153600 is rank 2, or document 30275282464153600 is rank 1 and document 30260724248870912 is rank 2. This logic applies to all other documents with identical scores.

The following scores are the result of one specific ***results.txt*** file:

With everything done and working, we went ahead and ran the **trec_eval script** to test our results with the qrels file that we were supplied with. To run the script, we used this command: *./trec_eval -m map -m P.10 trec_microblog11-qrels.txt results.txt*

After running for the MAP (Mean Average Precision and the P10 (Precision in the first 10 documents retrieved), these were our results:

```
map                   	all	0.2771
P_10                  	all	0.3020
```

MAP represents an overall performance of our searching, and we managed to achieve a 27.7% Mean Average Precision. 
Considering we have a limited data set, and our data set is only considered of tweets, we think this is pretty good.

Looking at the precision in the first 10 documents, we achieved 30.2% in precision. We think we could have achieved a higher
precision for the first 10 documents if we tweaked the pre-processing. With some better pre-processing, we believe the precision
for the first 10 documents could have been slightly higher, but overall we are satisfied with our results.

## Sample tokens from the vocabulary

Vocabulary size = 53310 words
```
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
```

## Sample queries

These queries are the result of one specific ***results.txt*** file.

### <ins>Query 3</ins>
"Haiti Aristide return"

#### Results



### <ins>Query 20</ins>
"Taco Bell filling lawsuit"

#### Results


