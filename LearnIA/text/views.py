from django.shortcuts import render
from text.funciones import algoritmo_function, comparacion_algoritmos

def text_index(request):
    return render(request, "text_index.html")

def graficos(request):
    algoritmo = request.POST['algoritmo']
    
    if(algoritmo == "Modelo Linear SVC"):
        parametroC = ""
        numArboles = ""
        profMaxima = ""
        funcMaximas = ""
        muestMaximas = ""
        muestRequeridas = ""
        iteraciones = request.POST['iteracionesSVC']
        polaridad = request.POST['polaridadSVC']
        
        ACC, ERR, SEN, ESP, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'title':algoritmo, 'ACC':ACC, 'ERR':ERR, 'SEN':SEN, 'ESP':ESP,  'TP':TP, 'FP':FP, 'TN':TN, 'FN':FN, 'TNONE':TNONE, 'FNONE':FNONE})
        
    elif(algoritmo == "Naives Bayes"):
        parametroC = ""
        numArboles = ""
        profMaxima = ""
        funcMaximas = ""
        muestMaximas = ""
        muestRequeridas = ""
        iteraciones = 0
        polaridad = request.POST['polaridadNB']
        
        
        ACC, ERR, SEN, ESP, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'title':algoritmo, 'ACC':ACC, 'ERR':ERR, 'SEN':SEN, 'ESP':ESP,  'TP':TP, 'FP':FP, 'TN':TN, 'FN':FN, 'TNONE':TNONE, 'FNONE':FNONE})
        
    elif(algoritmo == "Random Forest"):
        parametroC = ""
        iteraciones = 0
        polaridad = request.POST['polaridadRF']
        numArboles = request.POST['treeRF']
        profMaxima = request.POST['depthRF']
        funcMaximas = request.POST['featureRF']
        muestMaximas = request.POST['samSplitRF']
        muestRequeridas = request.POST['samLeafRF']
        
        ACC, ERR, SEN, ESP, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'title':algoritmo, 'ACC':ACC, 'ERR':ERR, 'SEN':SEN, 'ESP':ESP,  'TP':TP, 'FP':FP, 'TN':TN, 'FN':FN, 'TNONE':TNONE, 'FNONE':FNONE})
    
    elif(algoritmo == "Logistic Regression"):
        numArboles = ""
        profMaxima = ""
        funcMaximas = ""
        muestMaximas = ""
        muestRequeridas = ""
        iteraciones = 0
        polaridad = request.POST['polaridadLG']
        parametroC = request.POST['paramCLG']
        
        ACC, ERR, SEN, ESP, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'title':algoritmo, 'ACC':ACC, 'ERR':ERR, 'SEN':SEN, 'ESP':ESP,  'TP':TP, 'FP':FP, 'TN':TN, 'FN':FN, 'TNONE':TNONE, 'FNONE':FNONE})
    
    elif(algoritmo == "none"):
        ACC_LR, ACC_NB, ACC_SVC, ACC_RF, ERR_LR, ERR_NB, ERR_SVC, ERR_RF, SEN_LR, SEN_NB, SEN_SVC, SEN_RF, ESP_LR, ESP_NB, ESP_SVC, ESP_RF = comparacion_algoritmos()
        return render(request, "text_graph_gen.html", {'ACC_LR':ACC_LR, 'ACC_NB':ACC_NB, 'ACC_SVC':ACC_SVC, 'ACC_RF':ACC_RF, 'ERR_LR':ERR_LR, 'ERR_NB':ERR_NB, 'ERR_SVC':ERR_SVC, 'ERR_RF':ERR_RF, 'SEN_LR':SEN_LR, 'SEN_NB':SEN_NB, 'SEN_SVC':SEN_SVC, 'SEN_RF':SEN_RF, 'ESP_LR':ESP_LR, 'ESP_NB':ESP_NB, 'ESP_SVC':ESP_SVC, 'ESP_RF':ESP_RF})
    
    

 
    