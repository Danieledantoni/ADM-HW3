#!/usr/bin/env python
import json
from index_utils import processing
import pandas as pd
from utils import norm, calc_cos




def first_engine():
    
    with open('vocabulary.json', 'r') as myfile1:
        data=myfile1.read()
    voc = json.loads(data)

    with open('index1.json', 'r') as myfile1:
        data=myfile1.read()
    inv_index = json.loads(data)

    
    # here is the input query, after that we immediatly preprocess it
    query = input('search: ')
    query = processing(query)
    
    # we append in result list all documents that have he query words
    result = []
    # loop on the query words
    for word in query:
        # earch row of result corresponds to a word of the query
        w = []
        #  check the id of the word
        word_id = str(voc[word])
        for doc in inv_index[word_id]:
        # then check the documents corresponding to that id
            w.append(doc[0])
        result.append(w)
    # since we are interested in documents in which all the words appear we do the intersection
    # between all rows of result
    a = set(result[0])
    for i in range(1,len(result)):
        #a = set(result[i])
        a = a.intersection(set(result[i]))
    result = list(a)
    # save the documents in output dictionary, given the document id we import the tsv file to get the intro
    # and the link to the web page
    output = {'Title':[], 'Intro':[], 'Link':[]}
    for i in range(len(result)):
        try:
            movie = list(pd.pandas.read_csv('tsv_files2/movie_{}.tsv'.format(result[i]), encoding='utf-8', quotechar='"', delimiter='\t'))
        except:
            continue
        output['Title'].append(movie[0])
        output['Intro'].append(movie[1])
        output['Link'].append(movie[-1])
    print(pd.DataFrame(output).head())
    



def second_engine():
    
    with open('vocabulary.json', 'r') as myfile:
        data=myfile.read()
    voc = json.loads(data)

    
    with open('index1.json', 'r') as myfile1:
        data=myfile1.read()
    inv_index = json.loads(data)

    # here is the input query, after that we immediatly preprocess it
    query = input('search: ')
    query = processing(query)
    # the improve the search time we apply initially the first search engine on the new index

    # we append in result list all documents that have the query words
    result = []
    for word in query:
        w = []
        # first check the id
        word_id = str(voc[word])
        # then check the documents corresponding to that id
        for docs in inv_index[word_id]:
            w.append(docs[0])
        result.append(w)
    #result = list(set(result))
    
    a = set(result[0])
    for i in range(1,len(result)):
        #a = set(result[i])
        a = a.intersection(set(result[i]))
    result = list(a)

    
    # then save in a dictionary the documents id and the similarity
    sim = {'doc_id': [], 'similarity': []}
    # search only in documents that have the query words
    for doc in result:
        x = calc_cos(query, doc, inv_index, voc)
        if x != 0: 
            sim['doc_id'].append(doc)
            sim['similarity'].append(calc_cos(query,doc, inv_index, voc)/norm(doc, inv_index))
    
    pd.DataFrame(sim).sort_values(by= ['similarity'], ascending = False).head()
    #At this point we have all the documents id's and the similarities. Just need to print the desired data.
    output = {'Title':[], 'Intro':[], 'Link':[], 'Similarity':[]}
    for i in range(len(sim['doc_id'])):
        try:
            movie = list(pd.pandas.read_csv('tsv_files2/movie_{}.tsv'.format(sim['doc_id'][i]), encoding='utf-8', quotechar='"', delimiter='\t'))
        except FileNotFoundError:
            continue
        output['Title'].append(movie[0])
        output['Intro'].append(movie[1])
        output['Link'].append(movie[-1])
        output['Similarity'].append(sim['similarity'][i])
    print(pd.DataFrame(output).sort_values(by = ['Similarity'], ascending = False).head())


#Search Engine
print("Enter the Search Engine Number(1,2):")
choice = int(input())

if choice ==1:
    first_engine()
elif choice == 2:
    second_engine()

else:
    print("Wrong Choice")

