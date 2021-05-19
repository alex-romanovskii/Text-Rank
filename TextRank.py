#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functools import lru_cache
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import nltk
from nltk.stem.porter import *
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import glob
from itertools import combinations
import networkx as nx
import os
stop_words_set = set(stopwords.words("english"))
nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
path_files='texts/'
path_list=glob.glob(f'{path_files}*.txt')

new_path = f"{path_files}Summarize"
try:
    os.mkdir(new_path)
except OSError:
    pass

def skip_word(w):
    if len(w) < 2 or w in stop_words_set:
        return True
    return False

@lru_cache(maxsize=None)
def word_stemming(w):
    return stemmer.stem(w)  


def jaccard(first_set, second_set):
    index = 1.0
    if first_set or second_set:
        index = (float(len(first_set.intersection(second_set))) / len(first_set.union(second_set)))
    return index

def textrank(text,name):
    sentences = sent_tokenize(text)
    r=len(sentences)
    words_in_sentence = [set(word_stemming(word) for word in word_tokenize(sentence.lower()) if not skip_word(word) )
         for sentence in sentences]
    pairs = combinations(range(len(sentences)), 2)
    scores = [(i, j, jaccard(words_in_sentence[i], words_in_sentence[j])) for i, j in pairs]  
    g = nx.Graph()
    g.add_weighted_edges_from(scores)
    pr = nx.pagerank(g)
    result=sorted(((id,pr[id],sen) for id,sen in enumerate(sentences)),key=lambda x: x[0],reverse=False)    
    result=pd.DataFrame(result)
    result.columns=['Index','Weight','Sentence']
    result=result[['Index','Sentence','Weight']]
    scaler=MinMaxScaler()
    result['Weight']=scaler.fit_transform(result['Weight'].values.reshape(-1, 1))
    result.to_csv(new_path+'/'+name+'.csv',index=False)
    return result





