# -*- coding: utf-8 -*-
import requests
import io
 
from nltk.corpus import stopwords
from string import punctuation
import pandas as pd
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

spanish_stopwords = stopwords.words('spanish')

non_words = list(punctuation)
non_words.extend(['¡', '¿', '#'])
non_words.extend(map(str,range(10)))

stemmer = SnowballStemmer('spanish')

def algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC):
    data_p = read_csv(polaridad)

    data = data_p.dropna()

    sentences = data['sentence']
    polarities = data['label']

    sentences_procesed = clean_puntuaction(sentences)

    sentences_train, sentences_test, polarity_train, polarity_test = train_test_split(sentences_procesed, polarities, train_size=0.9)

    xtrain, xtest, vectorizer = train_test_counter_vector(xtrain=sentences_train, xtest=sentences_test)

    if(algoritmo == "Modelo Linear SVC"):
        classifier = LinearSVC(max_iter=int(iteraciones))
            
        classifier.fit(xtrain, polarity_train)
        pred = classifier.predict(xtest)
        
    elif(algoritmo == "Naives Bayes"):
        classifier = MultinomialNB()
        
        classifier.fit(xtrain, polarity_train)
        pred = classifier.predict(xtest)
        
    elif(algoritmo == "Random Forest"):
        classifier = RandomForestClassifier(n_estimators=int(numArboles), max_depth=int(profMaxima), min_samples_split=int(muestMaximas), min_samples_leaf=int(muestRequeridas), max_features=funcMaximas)
        
        classifier.fit(xtrain, polarity_train)
        pred = classifier.predict(xtest)
    
    elif(algoritmo == "Logistic Regression"):
        classifier = LogisticRegression(C=float(parametroC))
        
        classifier.fit(xtrain, polarity_train)
        pred = classifier.predict(xtest)

    TP, FP, TN, FN, TNONE, FNONE = perf_measure(polarity_test, pred, int(polaridad))
        
    total= TP + FP + TN + FN+ TNONE + FNONE
 
    #ACCURACY Y ERROR
    ACC = TP + TN + TNONE
    ERR = FP + FN + FNONE
    
    #SENSIBILIDAD Y ESPECIFIDAD 
    SEN_P = (TP/(TP + FN + FNONE))*100
    ESP_N = (TN/(TN + FP + FNONE))*100
    ESP_NONE = (TNONE/(TNONE + FP + FN))*100
    
    NSEN_P = (FP/(FP + TN + TNONE))*100
    NESP_N = (FN/(FN + TP + TNONE))*100
    NESP_NONE = (FNONE/(FNONE + TP + TN))*100
    
    return int(ACC), int(ERR), int(SEN_P), int(ESP_N), int(ESP_NONE), int(NSEN_P), int(NESP_N), int(NESP_NONE), int(TP), int(FP), int(TN), int(FN), int(TNONE), int(FNONE)
    
    
def comparacion_algoritmos():
    
    polaridad = 3
    
    data_p = read_csv(polaridad)

    data = data_p.dropna()

    sentences = data['sentence']
    polarities = data['label']

    sentences_procesed = clean_puntuaction(sentences)

    sentences_train, sentences_test, polarity_train, polarity_test = train_test_split(sentences_procesed, polarities, train_size=0.9)

    xtrain, xtest, vectorizer = train_test_counter_vector(xtrain=sentences_train, xtest=sentences_test)

    classifier_logistic_regression = LogisticRegression()
    classifier_logistic_regression.fit(xtrain, polarity_train)
    pred_logistic_reg = classifier_logistic_regression.predict(xtest)

    classifier_naives_bayes = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=False)
    classifier_naives_bayes.fit(xtrain, polarity_train)
    pred_naives_bayes = classifier_naives_bayes.predict(xtest)

    classifier_svm = LinearSVC()
    classifier_svm.fit(xtrain, polarity_train)
    pred_linear_SVC = classifier_svm.predict(xtest)

    classifier_random_forest = RandomForestClassifier()
    classifier_random_forest.fit(xtrain, polarity_train)
    pred_random_forest = classifier_random_forest.predict(xtest)

    TPLR, FPLR, TNLR, FNLR, TNONELR, FNONELR = perf_measure(polarity_test, pred_logistic_reg, polaridad)
    TPNB, FPNB, TNNB, FNNB, TNONENB, FNONENB = perf_measure(polarity_test, pred_naives_bayes, polaridad)
    TPSVC, FPSVC, TNSVC, FNSVC, TNONESVC, FNONESVC = perf_measure(polarity_test, pred_linear_SVC, polaridad)
    TPRF, FPRF, TNRF, FNRF, TNONERF, FNONERF = perf_measure(polarity_test, pred_random_forest, polaridad)
    
    totalLR = TPLR + FPLR + TNLR + FNLR + TNONELR + FNONELR
    totalNB = TPNB + FPNB + TNNB + FNNB + TNONENB + FNONENB
    totalSVC = TPSVC + FPSVC +  TNSVC + FNSVC + TNONESVC + FNONESVC
    totalRF = TPRF + FPRF + TNRF + FNRF + TNONERF + FNONERF 

    #ACCURACY Y ERROR
    ACC_LR = ((TPLR + TNLR + TNONELR)/totalLR)*100
    ACC_NB = ((TPNB + TNNB + TNONENB)/totalNB)*100
    ACC_SVC = ((TPSVC + TNSVC + TNONESVC)/totalSVC)*100
    ACC_RF = ((TPRF + TNRF + TNONERF)/totalRF)*100

    ERR_LR = ((FPLR + FNLR + FNONELR)/totalLR)*100
    ERR_NB = ((FPNB + FNNB + FNONENB)/totalNB)*100
    ERR_SVC = ((FPSVC + FNSVC + FNONESVC)/totalSVC)*100
    ERR_RF = ((FPRF + FNRF + FNONERF)/totalRF)*100
    
    #SENSIBILIDAD Y ESPECIFIDAD 
    SEN_LR_P = (TPLR/(TPLR + FNLR + FNONELR))*100
    SEN_NB_P = (TPNB/(TPNB + FNNB + FNONENB))*100
    SEN_SVC_P = (TPSVC/(TPSVC + FNSVC + FNONESVC))*100
    SEN_RF_P = (TPRF/(TPRF + FNRF + FNONERF))*100
    
    ESP_LR_N = (TNLR/(TNLR + FPLR + FNONELR))*100
    ESP_NB_N = (TNNB/(TNNB + FPNB + FNONENB))*100
    ESP_SVC_N = (TNSVC/(TNSVC + FPSVC + FNONESVC))*100
    ESP_RF_N = (TNRF/(TNRF + FPRF + FNONERF))*100
    
    ESP_LR_NONE = (TNONELR/(TNONELR + FPLR + FNLR))*100
    ESP_NB_NONE = (TNONENB/(TNONENB + FPNB + FNNB))*100
    ESP_SVC_NONE = (TNONESVC/(TNONESVC + FPSVC + FNSVC))*100
    ESP_RF_NONE = (TNONERF/(TNONERF + FPRF + FNRF))*100
    
    #Ratio de Falsos positivo y negativos (lo contrario a ENSIBILIDAD Y ESPECIFIDAD)
    NSEN_LR_P = (FPLR/(FPLR + TNLR + TNONELR))*100
    NSEN_NB_P = (FPNB/(FPNB + TNNB + TNONENB))*100
    NSEN_SVC_P = (FPSVC/(FPSVC + TNSVC + TNONESVC))*100
    NSEN_RF_P = (FPRF/(FPRF + TNRF + TNONERF))*100
    
    NESP_LR_N = (FNLR/(FNLR + TPLR + TNONELR))*100
    NESP_NB_N = (FNNB/(FNNB + TPNB + TNONENB))*100
    NESP_SVC_N = (FNSVC/(FNSVC + TPSVC + TNONESVC))*100
    NESP_RF_N = (FNRF/(FNRF + TPRF + TNONERF))*100
    
    NESP_LR_NONE = (FNONELR/(FNONELR + TPLR + TNLR))*100
    NESP_NB_NONE = (FNONENB/(FNONENB + TPNB + TNNB))*100
    NESP_SVC_NONE = (FNONESVC/(FNONESVC + TPSVC + TNSVC))*100
    NESP_RF_NONE = (FNONERF/(FNONERF + TPRF + TNRF))*100

    return int(ACC_LR), int(ACC_NB), int(ACC_SVC), int(ACC_RF), int(ERR_LR), int(ERR_NB), int(ERR_SVC), int(ERR_RF), int(SEN_LR_P), int(SEN_NB_P), int(SEN_SVC_P), int(SEN_RF_P), int(ESP_LR_N), int(ESP_NB_N), int(ESP_SVC_N), int(ESP_RF_N), int(ESP_LR_NONE), int(ESP_NB_NONE), int(ESP_SVC_NONE), int(ESP_RF_NONE), int(NSEN_LR_P), int(NSEN_NB_P), int(NSEN_SVC_P), int(NSEN_RF_P), int(NESP_LR_N), int(NESP_NB_N), int(NESP_SVC_N), int(NESP_RF_N), int(NESP_LR_NONE), int(NESP_NB_NONE), int(NESP_SVC_NONE), int(NESP_RF_NONE)


def demostracion(frase, algoritmo, polaridad,
                 iteraciones,
                 numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC):
    
    data_p = read_csv(polaridad)

    data = data_p.dropna()

    sentences = data['sentence']
    polarities = data['label']

    sentences_procesed = clean_puntuaction(sentences)
    
    sentences_serie = pd.Series(sentences_procesed)
    polarities_serie = pd.Series(polarities)
    frase_series = pd.Series(frase)
    
    vectorTrain, vectorizer = train_counter_vector(sentences_serie)
    
    vector = vectorizer.transform(frase_series)
        
    if(algoritmo == "Modelo Linear SVC"):
        classifier = LinearSVC(max_iter=int(iteraciones))
           
        classifier.fit(vectorTrain, polarities_serie)
        prediccion = classifier.predict(vector)
       
    elif(algoritmo == "Naives Bayes"):
        classifier = MultinomialNB()
        
        classifier.fit(vectorTrain, polarities_serie)
        prediccion = classifier.predict(vector)
         
    elif(algoritmo == "Random Forest"):
        classifier = RandomForestClassifier(n_estimators=int(numArboles), max_depth=int(profMaxima), min_samples_split=int(muestMaximas), min_samples_leaf=int(muestRequeridas), max_features=funcMaximas)
        
        classifier.fit(vectorTrain, polarities_serie)
        prediccion = classifier.predict(vector)
     
    elif(algoritmo == "Logistic Regression"):
        classifier = LogisticRegression(C=float(parametroC))
        
        classifier.fit(vectorTrain, polarities_serie)
        prediccion = classifier.predict(vector)
        
    if(prediccion[0] == 0):
        prediccion = "NEGATIVO";
        
    elif(prediccion[0] == 1):
        prediccion = "POSITIVO"
    
    else:
        prediccion = "NEUTRO"
        
    
    return frase, prediccion

def read_csv(polaridad):
    
    if(polaridad == '2'):
        url = "https://raw.githubusercontent.com/josnavmar/TFG/master/LearnIA/text/corpus/corpus_3000.csv"
    else:
        url = "https://raw.githubusercontent.com/josnavmar/TFG/master/LearnIA/text/corpus/corpus_4500.csv"
    



    s = requests.get(url).content
    
    result = pd.read_csv(io.StringIO(s.decode('utf-8')) , names=['sentence', 'label'], sep='\t', encoding='latin-1') 
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


def perf_measure(y_actual, y_hat, polaridad):
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
        if y_actual.get_values()[i]==y_hat[i]==3 and polaridad == 3:
            TNONE += 1
        if y_hat[i]==0 and y_actual.get_values()[i]!=y_hat[i] and polaridad == 3:
            FNONE += 1

    return(TP, FP, TN, FN, TNONE, FNONE)

def train_counter_vector(xtrain):
    vectorizer = CountVectorizer(tokenizer=tokenize,
       stop_words=spanish_stopwords, strip_accents='ascii') 
    vector_train = vectorizer.fit_transform(xtrain)
    
   
    return vector_train, vectorizer