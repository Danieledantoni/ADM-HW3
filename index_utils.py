import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
import re

# preprocessing a string, deleting stop words, and lemming
# this is needed for making the 
def processing(string):
    # we use the library nltk to remove stop words and do the lemming
    # convert all in lower case
    string = string.lower()
    # delete all but alphanumeric characters
    string = re.sub(r'\W+', ' ', string)
    # ge the set of stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(string) 
    # return string without stop words and after lemming
    return list([PorterStemmer().stem(x) for x in word_tokens if not x in stop_words])