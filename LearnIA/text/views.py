from django.shortcuts import render, render_to_response
from django.http import HttpResponse


from sklearn.model_selection import train_test_split
from text.funciones import read_csv, clean_puntuaction, train_test_counter_vector

import numpy as np
import matplotlib.pyplot as plt

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

from text.funciones import read_csv, clean_puntuaction, train_test_counter_vector, perf_measure
from _operator import pos, neg


from random import sample
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg

def text_index(request):
    return render(request, "text_index.html")

def text_graph(request):
    ACC_LR, ACC_NB, ACC_SVC, ACC_RF, ERR_LR, ERR_NB, ERR_SVC, ERR_RF, SEN_LR, SEN_NB, SEN_SVC, SEN_RF, ESP_LR, ESP_NB, ESP_SVC, ESP_RF = graph()
    
    return render(request, "text_graph.html", {'ACC_LR':ACC_LR, 'ACC_NB':ACC_NB, 'ACC_SVC':ACC_SVC, 'ACC_RF':ACC_RF, 'ERR_LR':ERR_LR, 'ERR_NB':ERR_NB, 'ERR_SVC':ERR_SVC, 'ERR_RF':ERR_RF, 'SEN_LR':SEN_LR, 'SEN_NB':SEN_NB, 'SEN_SVC':SEN_SVC, 'SEN_RF':SEN_RF, 'ESP_LR':ESP_LR, 'ESP_NB':ESP_NB, 'ESP_SVC':ESP_SVC, 'ESP_RF':ESP_RF})


def graph():
    
    data_p = read_csv()

    data = data_p.dropna()

    sentences = data['sentence']
    polarities = data['label']

    sentences_procesed = clean_puntuaction(sentences)

    sentences_train, sentences_test, polarity_train, polarity_test = train_test_split(sentences_procesed, polarities, train_size=0.8)

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

    TPLR, FPLR, TNLR, FNLR, TNONELR, FNONELR = perf_measure(polarity_test, pred_logistic_reg)
    TPNB, FPNB, TNNB, FNNB, TNONENB, FNONENB = perf_measure(polarity_test, pred_naives_bayes)
    TPSVC, FPSVC, TNSVC, FNSVC, TNONESVC, FNONESVC = perf_measure(polarity_test, pred_linear_SVC)
    TPRF, FPRF, TNRF, FNRF, TNONERF, FNONERF = perf_measure(polarity_test, pred_random_forest)
    
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
    SEN_LR = (TPLR/(TPLR + FNLR + FNONELR))*100
    SEN_NB = (TPNB/(TPNB + FNNB + FNONENB))*100
    SEN_SVC = (TPSVC/(TPSVC + FNSVC + FNONESVC))*100
    SEN_RF = (TPRF/(TPRF + FNRF + FNONERF))*100
    
    ESP_LR = (TNLR/(TNLR + FPLR + FNONELR))*100
    ESP_NB = (TNNB/(TNNB + FPNB + FNONENB))*100
    ESP_SVC = (TNSVC/(TNSVC + FPSVC + FNONESVC))*100
    ESP_RF = (TNRF/(TNRF + FPRF + FNONERF))*100
    

    
    return int(ACC_LR), int(ACC_NB), int(ACC_SVC), int(ACC_RF), int(ERR_LR), int(ERR_NB), int(ERR_SVC), int(ERR_RF), int(SEN_LR), int(SEN_NB), int(SEN_SVC), int(SEN_RF), int(ESP_LR), int(ESP_NB), int(ESP_SVC), int(ESP_RF)

    
    #buf = io.BytesIO()
    
    #plt.savefig(buf, format="png")

    # Creamos la respuesta enviando los bytes en tipo imagen png
    #response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    #response['Content-Length'] = str(len(response.content))


    # Limpiamos la figura para liberar memoria
    #ax.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    #response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    #return response