from django.shortcuts import render
from text.funciones import algoritmo_function, comparacion_algoritmos, demostracion

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
        
        ACC, ERR, SEN_P, ESP_N, ESP_NONE, NSEN_P, NESP_N, NESP_NONE, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'algoritmo':algoritmo,
                                                   'parametroC': parametroC, 'numArboles': numArboles,
                                                   'profMaxima': profMaxima, 'funcMaximas':funcMaximas,
                                                   'muestMaximas':muestMaximas, 'muestRequeridas':muestRequeridas,
                                                   'iteraciones':iteraciones,
                                                   'ACC':ACC, 'ERR':ERR, 
                                                   'SEN_P':SEN_P, 'ESP_N':ESP_N, 'ESP_NONE':ESP_NONE,
                                                   'NSEN_P':NSEN_P, 'NESP_N':NESP_N, 'NESP_NONE':NESP_NONE,
                                                   'TP':TP, 'FP':FP, 
                                                   'TN':TN, 'FN':FN, 
                                                   'TNONE':TNONE, 
                                                   'FNONE':FNONE})
        
    elif(algoritmo == "Naives Bayes"):
        parametroC = ""
        numArboles = ""
        profMaxima = ""
        funcMaximas = ""
        muestMaximas = ""
        muestRequeridas = ""
        iteraciones = 0
        polaridad = request.POST['polaridadNB']
        
        ACC, ERR, SEN_P, ESP_N, ESP_NONE, NSEN_P, NESP_N, NESP_NONE, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'algoritmo':algoritmo,
                                                   'parametroC': parametroC, 'numArboles': numArboles,
                                                   'profMaxima': profMaxima, 'funcMaximas':funcMaximas,
                                                   'muestMaximas':muestMaximas, 'muestRequeridas':muestRequeridas,
                                                   'iteraciones':iteraciones,
                                                   'ACC':ACC, 'ERR':ERR, 
                                                   'SEN_P':SEN_P, 'ESP_N':ESP_N, 'ESP_NONE':ESP_NONE,
                                                   'NSEN_P':NSEN_P, 'NESP_N':NESP_N, 'NESP_NONE':NESP_NONE,
                                                   'TP':TP, 'FP':FP, 
                                                   'TN':TN, 'FN':FN, 
                                                   'TNONE':TNONE, 
                                                   'FNONE':FNONE})
        
    elif(algoritmo == "Random Forest"):
        parametroC = ""
        iteraciones = 0
        polaridad = request.POST['polaridadRF']
        numArboles = request.POST['treeRF']
        profMaxima = request.POST['depthRF']
        funcMaximas = request.POST['featureRF']
        muestMaximas = request.POST['samSplitRF']
        muestRequeridas = request.POST['samLeafRF']
        
        ACC, ERR, SEN_P, ESP_N, ESP_NONE, NSEN_P, NESP_N, NESP_NONE, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'algoritmo':algoritmo,
                                                   'parametroC': parametroC, 'numArboles': numArboles,
                                                   'profMaxima': profMaxima, 'funcMaximas':funcMaximas,
                                                   'muestMaximas':muestMaximas, 'muestRequeridas':muestRequeridas,
                                                   'iteraciones':iteraciones,
                                                   'ACC':ACC, 'ERR':ERR, 
                                                   'SEN_P':SEN_P, 'ESP_N':ESP_N, 'ESP_NONE':ESP_NONE,
                                                   'NSEN_P':NSEN_P, 'NESP_N':NESP_N, 'NESP_NONE':NESP_NONE,
                                                   'TP':TP, 'FP':FP, 
                                                   'TN':TN, 'FN':FN, 
                                                   'TNONE':TNONE, 
                                                   'FNONE':FNONE})
    
    elif(algoritmo == "Logistic Regression"):
        numArboles = ""
        profMaxima = ""
        funcMaximas = ""
        muestMaximas = ""
        muestRequeridas = ""
        iteraciones = 0
        polaridad = request.POST['polaridadLG']
        parametroC = request.POST['paramCLG']
        
        ACC, ERR, SEN_P, ESP_N, ESP_NONE, NSEN_P, NESP_N, NESP_NONE, TP, FP, TN, FN, TNONE, FNONE = algoritmo_function(polaridad, iteraciones, algoritmo, numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
        return render(request, "text_graph.html", {'polaridad':polaridad, 'algoritmo':algoritmo,
                                                   'parametroC': parametroC, 'numArboles': numArboles,
                                                   'profMaxima': profMaxima, 'funcMaximas':funcMaximas,
                                                   'muestMaximas':muestMaximas, 'muestRequeridas':muestRequeridas,
                                                   'iteraciones':iteraciones,
                                                   'ACC':ACC, 'ERR':ERR, 
                                                   'SEN_P':SEN_P, 'ESP_N':ESP_N, 'ESP_NONE':ESP_NONE,
                                                   'NSEN_P':NSEN_P, 'NESP_N':NESP_N, 'NESP_NONE':NESP_NONE,
                                                   'TP':TP, 'FP':FP, 
                                                   'TN':TN, 'FN':FN, 
                                                   'TNONE':TNONE, 
                                                   'FNONE':FNONE})
    
    elif(algoritmo == "none"):
        ACC_LR, ACC_NB, ACC_SVC, ACC_RF, ERR_LR, ERR_NB, ERR_SVC, ERR_RF, SEN_LR_P, SEN_NB_P, SEN_SVC_P, SEN_RF_P, ESP_LR_N, ESP_NB_N, ESP_SVC_N, ESP_RF_N, ESP_LR_NONE, ESP_NB_NONE, ESP_SVC_NONE, ESP_RF_NONE, NSEN_LR_P, NSEN_NB_P, NSEN_SVC_P, NSEN_RF_P, NESP_LR_N, NESP_NB_N, NESP_SVC_N, NESP_RF_N, NESP_LR_NONE, NESP_NB_NONE, NESP_SVC_NONE, NESP_RF_NONE = comparacion_algoritmos()
        return render(request, "text_graph_gen.html", {'ACC_LR':ACC_LR, 'ACC_NB':ACC_NB, 'ACC_SVC':ACC_SVC, 'ACC_RF':ACC_RF, 'ERR_LR':ERR_LR, 'ERR_NB':ERR_NB, 'ERR_SVC':ERR_SVC, 'ERR_RF':ERR_RF, 
                                                       'SEN_LR_P':SEN_LR_P, 'SEN_NB_P':SEN_NB_P, 'SEN_SVC_P':SEN_SVC_P, 'SEN_RF_P':SEN_RF_P, 
                                                       'ESP_LR_N':ESP_LR_N, 'ESP_NB_N':ESP_NB_N, 'ESP_SVC_N':ESP_SVC_N, 'ESP_RF_N':ESP_RF_N,
                                                       'ESP_LR_NONE':ESP_LR_NONE, 'ESP_NB_NONE':ESP_NB_NONE, 'ESP_SVC_NONE':ESP_SVC_NONE, 'ESP_RF_NONE':ESP_RF_NONE,
                                                       'NSEN_LR_P':NSEN_LR_P, 'NSEN_NB_P':NSEN_NB_P, 'NSEN_SVC_P':NSEN_SVC_P, 'NSEN_RF_P':NSEN_RF_P, 
                                                       'NESP_LR_N':NESP_LR_N, 'NESP_NB_N':NESP_NB_N, 'NESP_SVC_N':NESP_SVC_N, 'NESP_RF_N':NESP_RF_N,
                                                       'NESP_LR_NONE':NESP_LR_NONE, 'NESP_NB_NONE':NESP_NB_NONE, 'NESP_SVC_NONE':NESP_SVC_NONE, 'NESP_RF_NONE':NESP_RF_NONE})
    
    

def demo_texto(request):
    frase = request.POST['inputDemo']
    algoritmo = request.POST['algoritmo']
    iteraciones = request.POST['iteraciones']
    polaridad = request.POST['polaridad']
    numArboles = request.POST['numArboles']
    profMaxima = request.POST['profMaxima']
    funcMaximas = request.POST['funcMaximas']
    muestMaximas = request.POST['muestMaximas']
    muestRequeridas = request.POST['muestRequeridas']
    parametroC = request.POST['parametroC']
    
    frase_predecida, prediccion = demostracion(frase, algoritmo, polaridad,
                               iteraciones,
                               numArboles, profMaxima, funcMaximas, muestMaximas, muestRequeridas, parametroC)
    
    return render(request, "text_demo.html", {'algoritmo':algoritmo, 'frase':frase_predecida, 'prediccion':prediccion})


        
  
    