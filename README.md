# search-engine
Naive Search engine on wikimedia dataset using Map-Reduce 

steps:

1. preprocess our dataset over the columns needed .
   
indexer:

2. create a vocabulary using the code in the vocab folder map-reduce paradigm.

3. create a TF for each word in the atricle using the map-reduce py files in the tf folder

4. create a document frequency using the map-reduce in the df folder.

5. calculate the idf scores for each article using the code in the score folder and the output produced from tf and df mapper and reducer.

6. finally convert the array into a vector space model using the code in vsm folder
