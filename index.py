 
import re
import csv
import pandas as pd
import json
from index_utils import processing
import numpy as np
with open('vocabulary.json', 'r') as myfile1:
    data=myfile1.read()
voc = json.loads(data)


#### FIRST INDEX #####

inv_index = {}
# import the tsv file
for i in range(1, 30001):
    # open the tsv file
    try:
        movie_input = list(pd.pandas.read_csv('tsv_files2/movie_{}.tsv'.format(i), encoding='utf-8', quotechar='"', delimiter='\t'))
    except FileNotFoundError:
        continue
        
    # for the first part we only need title intro and plot
    # we can join the title, the intro and the plot in the same string
    movie = ' '.join(movie_input[0:3])
    filt_movie = list(set(processing(movie)))
        
    # loop on the words of the filt_movie array
    for word in filt_movie:
        
        # check if the word id is in the keys, if it is update with the new document id       
        if voc[word] in inv_index.keys():
            inv_index[voc[word]].append(i)
        # if the word is not in the inv_index yet then add it 
        else:
            inv_index[voc[word]] = [i]
         
with open('inverted_index1.txt', 'w') as outfile:
    json.dump(inv_index, outfile)
    

#### SECOND INDEX #####

    
inv_index = {}

# import the tsv file
for i in range(1, 30001):
    # open the tsv file
    try:
        movie_input = list(pd.pandas.read_csv('tsv_files2/movie_{}.tsv'.format(i), encoding='utf-8', quotechar='"', delimiter='\t'))
    except FileNotFoundError:
        continue
        
    # we again only need title intro and plot
    # we can join the title, the intro and the plot in the same string
    movie = ' '.join(movie_input[0:3])
    filt_movie = list(processing(movie))
    #number of words present for the movie
    l = len(filt_movie)    
    # loop on the words of the filt_movie array
    for word in list(set(filt_movie)):
        # index of the word in the array voc
        
        #number of times the word present in the movie file
        n = list(filt_movie).count(word) 
        #calculating term frequency 
        tf = round(n/l,3)
        if voc[word] in inv_index.keys():
            #appending document id and term frequency of the word into the inv_index dictionary
            inv_index[voc[word]].append((i,tf))
        else:
            inv_index[voc[word]] = [(i,tf)]
            
# total documents ids
docs = []
for x in inv_index.values():
    for y in x:
        docs.append(y[0])
docs = list(set(docs))
# number of total documents
N = len(docs)          
# the idf term is the same for all documents of the respective word
for word_id in inv_index:
    # first we count the number of documents the word appears in 
    cont = 0
    for doc in inv_index[word_id]:
        cont += 1
    # then evaluate the idf term  
    idf = np.log(N/cont)
    #print(word_id, idf)
    # then update the inv_index with the tfidf terms.
    for doc in inv_index[word_id]:
        doc = list(doc)
        doc[1] *= idf
            
with open('inverted_index2.txt', 'w') as outfile:
    json.dump(inv_index, outfile)