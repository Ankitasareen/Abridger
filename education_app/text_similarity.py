import nltk
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode
import string
import numpy as np
import re
from collections import Counter
import itertools
from sklearn.metrics.pairwise import cosine_similarity
import gensim.downloader as api
import streamlit as st

def preprocess_text(text):
    text = re.sub(r'\[[0-9]*\]',' ', text)
    text = re.sub(r'\s+',' ',text)
    text = text.lower()
    text = re.sub(r'\d',' ',text)
    text = re.sub(r'\s+',' ',text)
    stopset = stopwords.words('english') + list(string.punctuation)
    text = " ".join([i for i in word_tokenize(text) if i not in stopset])
    text = unidecode(text)
    return text

def word_emb_model():
    return KeyedVectors.load_word2vec_format("/home/abhrant/Projects/Education_App/gensim-data/glove-twitter-200/glove-twitter-200.gz")
word_emb_model = word_emb_model()

def map_word_frequency(document):
    return Counter(itertools.chain(*document))


def get_sif_feature_vectors(sentence1, sentence2, word_emb_model=word_emb_model):
    sentence1 = [token for token in sentence1.split() if token in word_emb_model.wv.vocab]
    sentence2 = [token for token in sentence2.split() if token in word_emb_model.wv.vocab]
    word_counts = map_word_frequency((sentence1 + sentence2))
    embedding_size = 200 
    a = 0.001
    sentence_set=[]
    for sentence in [sentence1, sentence2]:
        vs = np.zeros(embedding_size)
        sentence_length = len(sentence)
        for word in sentence:
            a_value = a / (a + word_counts[word]) 
            vs = np.add(vs, np.multiply(a_value, word_emb_model.wv[word]))
        if sentence_length != 0: 
            vs = np.divide(vs, sentence_length) 
            sentence_set.append(vs)
    return sentence_set

def get_cosine_similarity(feature_vec_1, feature_vec_2):    
    return cosine_similarity(feature_vec_1.reshape(1, -1), feature_vec_2.reshape(1, -1))[0][0]



def get_similarity(true_answer , user_answer):
    i=0
    mark_list = []
    for i in range(len(user_answer)):
        sent_1 = preprocess_text(true_answer[i])
        sent_2 = preprocess_text(user_answer[i])

        sent_set=get_sif_feature_vectors(sent_1,sent_2,word_emb_model)
        cos_sim = get_cosine_similarity(sent_set[0],sent_set[1])
        mark_list.append(cos_sim >= 0.75)            
    
    return mark_list