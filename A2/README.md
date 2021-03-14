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

For this assignment, we took the code of our Assignment 1, and made small modifications in order to do some experiments on it.

For experiment 1,...

For experiment 2, not much was needed to be changed in terms of the code. The goal of this experiment was to do some query vector modification or query expansince based on pretrained word embeddings. We ended up using a Word2Vec model built on a Twitter Corpus and some code built by Loreto Parisi which we found on GitHub. (https://github.com/loretoparisi/word2vec-twitter) This code allowed us to run our previous code without many changes. The code we found on GitHub allowed us to find similar words for the words that appeared in each query. By finding those similar words or synonyms, it allowed us to expand the query. 

After expanding the query, we needed to re-vectorize the query. To do that, we just used the code we previously built for assignment 1, but with some slight modifications given that we were passing a list of in the function instead of a full query. With the query re-vectorized, we were able to build new results and test them using the TREC evaluation method. Those results can be found in the ***Results*** section of this file.

### Future changes
Currently, a problem is that part of our preprocessing code can be found in 2 separate Python files (***preprocessor.py*** and ***query.py***). This means we have some duplicate code. In the future, we plan on storing this function in one place, and having both locations call to this one function. That way, future changes to our preprocessing would only require modification in one location.

## Results

### Previous Results 

```
map                   	all	0.2771
P_10                  	all	0.3020
```


### Experiment 1

Results

```
map                   	all	0.
P_10                  	all	0.
```

### Experiment 2

Results

Looking at theses results, we can see that they are not as good as the results we achieved in our first assignment. Query expansion itself is used to increase the quality of the search results but that comes at the expense of precision. This is why we're seeing a lower MAP and a lower Precision for the first 10 documents.

```
map                   	all	0.2076
P_10                  	all	0.1735
```


## Sample queries

### Experiment 1

These queries are the result of one specific ***results.txt*** file.

### <ins>Query 3</ins>
"Haiti Aristide return"

#### Results



### <ins>Query 20</ins>
"Taco Bell filling lawsuit"

#### Results

### Experiment 2

These queries are the result running exeperiment number 2

### <ins>Query 3</ins>
"Haiti Aristide return"

#### Results

1. 34950800157450240	John Baer: Who didn't see this coming?: TO THOSE who know Ed and Midge Rendell - heck, to the Philly world at la... http://bit.ly/ii6WEO

2. 29555143699603456	1-2-3 Spa! Relax and Unwind at Half Moon, A RockResort. Book 3 nights or more at Half Moon Jamaica, and receive a... http://fb.me/NXexbkC6

3. 33274580210556928	http://go-jamaica.com/news/read_article.php?id=26130 #Jamaica #Prime Mnister to launch #climatechange programme

4. 30702782788927489	feednews: Jamaica: “Dog-Paw”: Written by Janine Mendes-Franco “The cliche that truth is stranger than fiction is... http://bit.ly/gKF45u

5. 30701708191465472	Jamaica: “Dog-Paw”: Written by Janine Mendes-Franco “The cliche that truth is stranger than fiction is true”: Ac... http://bit.ly/hPf8SD

6. 34768755347169280	LIRR service is experiencing eastbound delays between 5 to 10 minutes through Jamaica due to an earlier train with equipment problems.

7. 28984571475271680	RT @Joe_Taxi: RT @mediahacker: S. Africa and Cuba negotiating to facilitate return of Aristide http://www.timeslive.co.za/sundaytimes/article866448.ece/I-want-to-go-home-says-Haitis-Aristide … #Haiti

8. 29296574815272960	Haiti – Aristide : His return, an international affair… – Haitilibre.com http://bit.ly/gzyLXG #haiti

9. 32387196078006272	Haiti allows ex-president's return: Jean-Bertrand Aristide, who was Haiti's first democratically elected leader,... http://aje.me/fQ4j4T

10. 32211683082502144	#int'l #news: Haiti opens door for return of ex-president Aristide: PORT-AU-PRINCE (Reuters) - Haiti'... http://bit.ly/gSIFwd #singapore


### <ins>Query 20</ins>
"Taco Bell filling lawsuit"

#### Results

1. 29906116062220290	Lawsuit: Taco Bell Ground Beef Is Really Just "Meat Filling" - @consumerist http://consumerist.com/2011/01/lawsuit-says-taco-bell-ground-beef-is-really-just-taco-meat-filling.html?utm_source=streamsend&utm_medium=email&utm_content=13297631&utm_campaign=Fo

2. 31082136219947008	Taco Bell Counters 'Meat Filling' Charges in Lawsuit With Print, Web Effort http://goo.gl/fb/H9wcB

3. 31043176684851200	Oxymoron alert: "The lawsuit is bogus & filled with completely inaccurate facts" Taco Bell President said. Inaccurate facts? Freudian slip?

4. 29853985930219520	That ain't necessarily "beef" in your Taco Bell burrito...a new lawsuit wants the chain to label it "taco meat filling" instead.

5. 30344959127191552	Obama: Let's rein in frivolous lawsuits. Kucinich then sues House cafeteria over olive pit in sandwich. #badtiming http://bit.ly/fgFk1j

6. 30986819369697281	@nflnetwork "The Rudy Rule" Sounds Like Something To Prevent Lawsuits. Black Players,coaches,& GM's Should All The Opportunity As White Ones

7. 32443636847218688	The Ins And Out Of Small Claims: Filling a civil lawsuit against an organization or person in hopes of col... http://tinyurl.com/4s8h474

8. 29158340424634368	Lawsuit Loans – Filling the Need For Funding http://bit.ly/hYuw1C

9. 30700675742572545	I wonder what makes all the people who want taco bell to go vegetarian think that they will put real vegetables in the filling.

10. 30012275423186944	Hey, @H0TMessBarbie, you hear Taco Bell is being sued because their beef filling is only 35% beef? I told you it makes a good enema!

