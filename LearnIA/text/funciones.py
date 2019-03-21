# -*- coding: utf-8 -*- 
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer

spanish_stopwords = stopwords.words('spanish')

non_words = list(punctuation)
non_words.extend(['¡', '¿', '#'])
non_words.extend(map(str,range(10)))

stemmer = SnowballStemmer('spanish')

def read_csv():
    dirPathToCsv = 'C:/Users/PC-8888/eclipse-workspace/TFG/LearnIA//text/corpus/'
    result = pd.read_csv(dirPathToCsv + 'corpus_4500.csv' , names=['sentence', 'label'], sep='\t', encoding='latin-1')
    
    return result

def cut_corpus(sentences, polarities):
    

    #chunks = [data[x:x+100] for x in range(0, len(data), 100)]
    
    train_sentences = [sentences[3000:4000]]
    test_setences = []
    
    
    return train_sentences, test_setences


def clean_puntuaction(data):
    result = []
    
    for text in data:
        text = ''.join([c for c in text if c not in non_words])
        
        result.append(text)
        
    return result

def tokenize(text):
    #tokens = [i for i in word_tokenize(text, language='spanish') if i not in spanish_stopwords]
    tokens =  word_tokenize(text, language='spanish')
 
    try:
        stems = stem_tokens(tokens, stemmer)
    except Exception as e:
        print(e)
        stems = ['']   
        
    return stems

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def train_test_counter_vector(xtrain, xtest):
    vectorizer = CountVectorizer(tokenizer=tokenize,
       stop_words=spanish_stopwords, strip_accents='ascii') 
    vector_train = vectorizer.fit_transform(xtrain)
    
    vector_test = vectorizer.transform(xtest)
   
    return vector_train, vector_test, vectorizer

def train_test_tfid_vector(xtrain, xtest):
    vectorizer = TfidfVectorizer(tokenizer=tokenize,
       stop_words=spanish_stopwords, strip_accents='ascii') 
    vector_train = vectorizer.fit_transform(xtrain)
    
    vector_test = vectorizer.transform(xtest)
   
    return vector_train, vector_test, vectorizer


def train_test_tfid_vector_transformer(xtrain, xtest):
    vectorizer = CountVectorizer(tokenizer=tokenize,
       stop_words=spanish_stopwords, strip_accents='ascii') 
    vector_train = vectorizer.fit_transform(xtrain)
    
    vector_test = vectorizer.transform(xtest)
    
    tfidf_transformer = TfidfTransformer()
    tfidf_mat_train = tfidf_transformer.fit_transform(vector_train)
    tfidf_mat_test = tfidf_transformer.fit_transform(vector_test)
   
    return tfidf_mat_train, tfidf_mat_test, vectorizer


def perf_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    TNONE = 0
    FNONE = 0

    for i in range(len(y_hat)): 
        if y_actual.get_values()[i]==y_hat[i]==1:
            TP += 1
        if y_hat[i]==1 and y_actual.get_values()[i]!=y_hat[i]:
            FP += 1
        if y_actual.get_values()[i]==y_hat[i]==0:
            TN += 1
        if y_hat[i]==0 and y_actual.get_values()[i]!=y_hat[i]:
            FN += 1
        if y_actual.get_values()[i]==y_hat[i]==3:
            TNONE += 1
        if y_hat[i]==0 and y_actual.get_values()[i]!=y_hat[i]:
            FNONE += 1

    return(TP, FP, TN, FN, TNONE, FNONE)