# search-engine
Naive Search engine on wikimedia dataset using Map-Reduce 

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

   

8. calculate the idf scores for each article using the code in the score folder and the output produced from tf and df mapper and reducer.

9. finally convert the array into a vector space model using the code in vsm folder

the above provided steps perform 80 % of the work that includes handling the dataset and how it is to be processes in each map reduce. While the below steps are now to be performed for the query, query vectorizer and ranking of articles.
