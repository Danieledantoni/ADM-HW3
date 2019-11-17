import math

# given the document id we evaluate its norm
def norm (doc_id, inv_index):
    norm = 0
    for word_id in inv_index:
        for doc in inv_index[word_id]:
            if doc[0] == doc_id:
                norm += doc[1]*doc[1]
    return math.sqrt(norm)


# this is the function that returns the similarity

# the document vector is alredy normalized, so we just need to compute the dot product between the query 
# vector and the document
def calc_cos (query, doc_id, inv_index, voc):
    dot_p = 0
    for words in query:
        word_id = str(voc[words])
        for docs in inv_index[word_id]:
            if docs[0] == doc_id:
                dot_p += docs[1]
    return(dot_p/math.sqrt(len(query)))
