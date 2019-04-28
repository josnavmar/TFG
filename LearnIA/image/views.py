from django.shortcuts import render
from image.funciones import sentgen_function
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from image.funciones import demostracion, desgeneraliza


import math 
from LearnIA.settings import BASE_DIR

def image_index(request):
    return render(request, "image_index.html")

def graficos_imagen(request):
    sentgen = request.POST['SentGen']
        
    if(sentgen == "Sentimiento"):
        
        red = request.POST['redSent']
        iteracciones = request.POST['iteraccionSent']
        optimizador = request.POST['optimizadorSent']
                
        AEN,FEN,AAS,FAS,AMI,FMI,AFE,FFE,ATR,FTR,ASO,FSO,ANE,FNE,AMA,FMA,AFEM,FFEM, model = sentgen_function(sentgen,red,iteracciones,optimizador)
        
        ACC = AEN + AAS + AMI + AFE + ATR + ASO + ANE
        ERR = FEN + FAS + FMI + FFE + FTR + FSO + FNE
        
        SEN_FE = math.trunc((AFE/(AFE + FEN + FAS + FMI + FTR + FSO + FNE))*100)
        ESP_AS = math.trunc((AAS/(AAS + FEN+ FFE + FMI + FTR + FSO + FNE))*100)
        ESP_EN = math.trunc((AEN/(AEN + FAS+ FFE + FMI + FTR + FSO + FNE))*100)
        ESP_MI = math.trunc((AMI/(AMI + FAS+ FFE + FEN + FTR + FSO + FNE))*100)
        ESP_TR = math.trunc((ATR/(ATR + FAS+ FFE + FMI + FEN + FSO + FNE))*100)
        ESP_SO = math.trunc((ASO/(ASO + FAS+ FFE + FMI + FEN + FTR + FNE))*100)
        ESP_NE = math.trunc((ASO/(ASO + FAS+ FFE + FMI + FEN + FTR + FSO))*100)
                
        return render(request, "image_graph.html", {'title':sentgen, 'red':red, 'AEN':AEN, 'FEN':FEN,
                      'AAS':AAS, 'FAS':FAS, 'AMI':AMI, 'FMI':FMI, 'AFE':AFE, 'FFE':FFE, 'ATR':ATR,
                      'FTR':FTR, 'ASO':ASO, 'FSO':FSO, 'ANE':ANE, 'FNE':FNE, 'AMA':AMA, 'FMA':FMA,
                      'AFEM':AFEM, 'FFEM':FFEM, 'ACC':ACC, 'ERR':ERR, 'SEN_FE':SEN_FE, 'ESP_AS':ESP_AS, 'ESP_EN':ESP_EN,
                      'ESP_MI':ESP_MI, 'ESP_TR':ESP_TR, 'ESP_SO':ESP_SO, 'ESP_NE':ESP_NE, 'model':model})
        
    elif(sentgen == "Genero"):
        
        red = request.POST['redGen']
        iteraciones = request.POST['iteraccionGen']
        optimizador = request.POST['optimizadorGen']
        
        AEN,FEN,AAS,FAS,AMI,FMI,AFE,FFE,ATR,FTR,ASO,FSO,ANE,FNE,AMA,FMA,AFEM,FFEM, model = sentgen_function(sentgen,red,iteraciones,optimizador)
        
        ACC = AMA + AFEM
        ERR = FMA + FFEM
        
        SEN_MA = math.trunc((AMA/(AMA + FFEM))*100)
        ESP_FEM = math.trunc((AFEM/(AFEM + FMA))*100)
        
        return render(request, "image_graph.html", {'title':sentgen, 'red':red, 'AEN':AEN, 'FEN':FEN,
                      'AAS':AAS, 'FAS':FAS, 'AMI':AMI, 'FMI':FMI, 'AFE':AFE, 'FFE':FFE, 'ATR':ATR,
                      'FTR':FTR, 'ASO':ASO, 'FSO':FSO, 'ANE':ANE, 'FNE':FNE, 'AMA':AMA, 'FMA':FMA,
                      'AFEM':AFEM, 'FFEM':FFEM, 'ACC':ACC, 'ERR':ERR , 'SEN_MA':SEN_MA, 'ESP_FEM':ESP_FEM, 'model':model})
        

def image_upload(request):
    
    sentgen = request.POST['sentgen']
    model = request.POST['model']
    path=''
    prediccion_text = ''
    emotion_text = ''
    gender_text = ''
        
    if request.method == 'POST' and request.FILES['inputDemo']:
        myfile = request.FILES['inputDemo']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        if(sentgen == 'Sentimiento'):
            path = '/image/trained_models/emotion_models/'
            emotion_text, gender_text = demostracion(uploaded_file_url, model, path, sentgen)
            prediccion_text = desgeneraliza(emotion_text)
            
        elif(sentgen == 'Genero'):
            path = '/image/trained_models/gender_models/'
            emotion_text, gender_text = demostracion(uploaded_file_url, model, path, sentgen)
            prediccion_text = gender_text
        else:
            print('ERROR PARAMETRO PATH NULO')
        
        print(uploaded_file_url)
        
        if(prediccion_text ==''):
            prediccion_text = 'No se ha detectado rostro'
        else:
            prediccion_text = prediccion_text
            
        
        return render(request, 'image_demo.html', {
            'uploaded_file_url': uploaded_file_url,
            'filename':myfile.name, 'prediccion_text':prediccion_text
        })
    return render(request, 'index')
