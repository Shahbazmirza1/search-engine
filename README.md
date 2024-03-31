# search-engine
Naive Search engine on wikimedia dataset using Apache Hadoop. 

overview: 
In this repository we have created a Naive search engine using the wikimedia dataset that contains 5 million rows of data with article_id and article_text.
out approach to resolve this task is done using Apache Hadoop Map-reduce paradigm and its components . 

requirements: 
1. Hadoop-3.3.6
2. Access to the dataset .



the below are the steps to utilise this repository code with the approach explained .
steps:

1. preprocess our dataset over the columns needed .
   
indexer:

2. create a vocabulary using the code in the vocab folder map-reduce paradigm.
   Input : preprocessed dataset
   output: a txt file containing a unique index for each word thus vocabulary.

4. create a TF for each word in the atricle using the map-reduce py files in the tf folder.
   Input: the preprcoessed dataset , While the mapper in the tf folder has to been given the path to the vocab.txt created and copied to the local drive.
   output: it contains terms and its frequencies for each article in this format  ({article_id}:{tf_list})

6. create a document frequency using the map-reduce in the df folder.
   Input: the tf.txt created above by the mapper and reducer.
   output: it contains the each term and total articles that is appears in.this format  {current_word_id}\t{len(articles)}

   

7. calculate the inverted document frequency scores for each article using the code in the score folder.
   input : the tf.txt generated and make sure to change the path in the mapper for df.txt produced aswell .
   output : the out put is the same as tf but the scores are normalized in-terms with the document frequncy.
    

8. finally convert the array into a vector space model using the code in vsm folder.
    Input : give the score out put to this.
    OUTPUT : each document-id along with word_id:idf scores are given as output in shape of a vector.

the above provided steps perform 80 % of the work that includes handling the dataset and how it is to be processes in each map reduce. While the below steps are now to be performed for the query, query vectorizer and ranking of articles.

9. QUERY:
    Initially run the query.py with the query in it.
    out put : the output will be the word_id and term frequency for the query.

10. Secondly run the mapper and reducer in the query folder with the query.txt created by the python code before.
    out put: the output contains the query vector that is to be compared with each document vector in the next-step

11. Ranking:
    input: give the document vectors created using the vsm to the ranking mapper and reducer as input.
    output : it will consist of top 10 documents with which the query matches with .

    Tada !! you finally have a naive search engine.
