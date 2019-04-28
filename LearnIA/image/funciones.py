# -*- coding: utf-8 -*-
import sys
import cv2
from keras.models import load_model
import numpy as np
from django import forms
from LearnIA.settings import BASE_DIR, BASE_DIR_RE

from image.src.utils.datasets import get_labels
from image.src.utils.inference import detect_faces
from image.src.utils.inference import draw_text
from image.src.utils.inference import draw_bounding_box
from image.src.utils.inference import apply_offsets
from image.src.utils.inference import load_detection_model
from image.src.utils.inference import load_image
from image.src.utils.preprocessor import preprocess_input



def sentgen_function(sentgen,red, iteracciones, optimizador):
    
    AEN = 0
    FEN = 0
            
    AAS = 0
    FAS = 0
            
    AMI = 0
    FMI = 0
            
    AFE = 0
    FFE = 0
            
    ATR = 0
    FTR = 0
            
    ASO = 0
    FSO = 0
            
    ANE = 0
    FNE = 0
    
    AMA = 0 
    FMA = 0
    
    AFEM = 0
    FFEM = 0
    
    model = ''
      
#SENTIMIENTO--------------------------------------------------------------------------------------------------
    if sentgen == 'Sentimiento':
#        SIMPLE CNN------------------------------------------------------------------------
        if red == 'Simple CNN' and optimizador == 'Adam' and iteracciones == '25'  :
            
            AEN = 315
            FEN = 643
            
            AAS = 0
            FAS = 111
            
            AMI = 358
            FMI = 666
            
            AFE = 798
            FFE = 976
            
            ATR = 448
            FTR = 799
            
            ASO = 265
            FSO = 566
            
            ANE = 123
            FNE = 1110
            
            model = 'fer2013_simple_CNN(adam,acc).02-0.33.hdf5'
            
            
        elif red == 'Simple CNN' and optimizador == 'Adam' and iteracciones == '50'  :
            
            AEN = 420
            FEN = 565
            
            AAS = 21
            FAS = 90
            
            AMI = 491
            FMI = 533
            
            AFE = 993
            FFE = 781
            
            ATR = 615
            FTR = 632
            
            ASO = 357
            FSO = 474
            
            ANE = 271
            FNE = 962
            
            model = 'fer2013_simple_CNN(adam,acc).03-0.45.hdf5'
            
        elif red == 'Simple CNN' and optimizador == 'Adam' and iteracciones == '100'  :
            
            AEN = 480
            FEN = 478
            
            AAS = 39
            FAS = 72
            
            AMI = 532
            FMI = 492
            
            AFE = 1233
            FFE = 541
            
            ATR = 785
            FTR = 462
            
            ASO = 522
            FSO = 309
            
            ANE = 403
            FNE = 830
            
            model = 'fer2013_simple_CNN(adam,acc).13-0.54.hdf5'
            
         
        elif red == 'Simple CNN' and optimizador == 'SGD' and iteracciones == '25'  :
            
            AEN = 218
            FEN = 719
            
            AAS = 9
            FAS = 102
            
            AMI = 330
            FMI = 694
            
            AFE = 931
            FFE = 843
            
            ATR = 620
            FTR = 627
            
            ASO = 342
            FSO = 489
            
            ANE = 147
            FNE = 1086
            
            model = 'fer2013_simple_CNN(sgd,acc).03-0.35.hdf5'
            
            
        elif red == 'Simple CNN' and optimizador == 'SGD' and iteracciones == '50'  :
            
            AEN = 422
            FEN = 536
            
            AAS = 21
            FAS = 90
            
            AMI = 511
            FMI = 513
            
            AFE = 1299
            FFE = 475
            
            ATR = 783
            FTR = 464
            
            ASO = 432
            FSO = 399
            
            ANE = 361
            FNE = 872
            
            model = 'fer2013_simple_CNN(sgd,acc).26-0.53.hdf5'
            
        
        elif red == 'Simple CNN' and optimizador == 'SGD' and iteracciones == '100'  :
            
            AEN = 433
            FEN = 525
            
            AAS = 27
            FAS = 84
            
            AMI = 511
            FMI = 513
            
            AFE = 1314
            FFE = 460
            
            ATR = 820
            FTR = 427
            
            ASO = 432
            FSO = 399
            
            ANE = 383
            FNE = 850
            
            model = 'fer2013_simple_CNN(sgd,acc).34-0.55.hdf5'
            
        
        elif red == 'Simple CNN' and optimizador == 'RMSprop' and iteracciones == '25'  :
            
            AEN = 453
            FEN = 505
            
            AAS = 11
            FAS = 100
            
            AMI = 444
            FMI = 580
            
            AFE = 966
            FFE = 808
            
            ATR = 448
            FTR = 799
            
            ASO = 285
            FSO = 546
            
            ANE = 166
            FNE = 1067
            
            model = 'fer2013_simple_CNN(kms,acc).03-0.39.hdf5'
            
            
        elif red == 'Simple CNN' and optimizador == 'RMSprop' and iteracciones == '50'  :
            
            AEN = 433
            FEN = 525
            
            AAS = 28
            FAS = 83
            
            AMI = 496
            FMI = 528
            
            AFE = 1168
            FFE = 546
            
            ATR = 765
            FTR = 482
            
            ASO = 520
            FSO = 311
            
            ANE = 275
            FNE = 958
            
            model = 'fer2013_simple_CNN(kms,acc).13-0.51.hdf5'
            
        elif red == 'Simple CNN' and optimizador == 'RMSprop' and iteracciones == '100'  :
            
            AEN = 445
            FEN = 513
            
            AAS = 33
            FAS = 78
            
            AMI = 511
            FMI = 513
            
            AFE = 1384
            FFE = 390
            
            ATR = 820
            FTR = 427
            
            ASO = 435
            FSO = 396
            
            ANE = 383
            FNE = 850
            
            model = 'fer2013_simple_CNN(kms,acc).27-0.56.hdf5'
            
#        MINI XCEPTION CNN------------------------------------------------------------------------       
        elif red == 'Mini XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '25'  :
            
            AEN = 408
            FEN = 550
            
            AAS = 19
            FAS = 92
            
            AMI = 507
            FMI = 517
            
            AFE = 1287
            FFE = 487
            
            ATR = 783
            FTR = 464
            
            ASO = 432
            FSO = 399
            
            ANE = 361
            FNE = 872
            
            
            model = 'fer2013_mini_XCEPTION.02-0.52.hdf5'
            
        elif red == 'Mini XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '50'  :
            
            AEN = 523
            FEN = 435
            
            AAS = 34
            FAS = 77
            
            AMI = 625
            FMI = 399
            
            AFE = 1343
            FFE = 431
            
            ATR = 824
            FTR = 423
            
            ASO = 546
            FSO = 285
            
            ANE = 314
            FNE = 919
        
            model = 'fer2013_mini_XCEPTION.09-0.58.hdf5'
            
            
        elif red == 'Mini XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '100'  :
            
            AEN = 666
            FEN = 292
            
            AAS = 44
            FAS = 67
            
            AMI = 701
            FMI = 323
            
            AFE = 1382
            FFE = 392
            
            ATR = 877
            FTR = 370
            
            ASO = 628
            FSO = 211
            
            ANE = 428
            FNE = 805
            
            model = 'fer2013_mini_XCEPTION.107-0.66.hdf5'
            
         
        elif red == 'Mini XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '25'  :
            
            AEN = 462
            FEN = 496
            
            AAS = 0
            FAS = 111
            
            AMI = 555
            FMI = 469
            
            AFE = 989
            FFE = 785
            
            ATR = 577
            FTR = 670
            
            ASO = 309
            FSO = 522
            
            ANE = 122
            FNE = 1111
            
            model = 'fer2013_mini_XCEPTION(sgd,acc).04-0.41.hdf5'
            
            
        elif red == 'Mini XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '50'  :
            
            AEN = 574
            FEN = 384
            
            AAS = 12
            FAS = 99
            
            AMI = 588
            FMI = 436
            
            AFE = 1120
            FFE = 654
            
            ATR = 615
            FTR = 632
            
            ASO = 430
            FSO = 401
            
            ANE = 271
            FNE = 962
            
            model = 'fer2013_mini_XCEPTION(sgd,acc).13-0.51.hdf5'
            
        
        elif red == 'Mini XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '100'  :
            
            AEN = 574
            FEN = 384
            
            AAS = 14
            FAS = 97
            
            AMI = 701
            FMI = 323
            
            AFE = 1254
            FFE = 520
            
            ATR = 630
            FTR = 617
            
            ASO = 580
            FSO = 251
            
            ANE = 301
            FNE = 932
            
            model = 'fer2013_mini_XCEPTION(sgd,acc).35-0.57.hdf5'
            
        
        elif red == 'Mini XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '25'  :
            
            AEN = 417
            FEN = 541
            
            AAS = 5
            FAS = 106
            
            AMI = 521
            FMI = 503
            
            AFE = 987
            FFE = 787
            
            ATR = 615
            FTR = 632
            
            ASO = 333
            FSO = 498
            
            ANE = 271
            FNE = 962
            
            model = 'fer2013_mini_XCEPTION(rmsprop,acc).03-0.44.hdf5'
            
            
        elif red == 'Mini XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '50'  :
            
            AEN = 493
            FEN = 465
            
            AAS = 25
            FAS = 86
            
            AMI = 589
            FMI = 435
            
            AFE = 1391
            FFE = 383
            
            ATR = 797
            FTR = 450
            
            ASO = 514
            FSO = 317
            
            ANE = 351
            FNE = 882 
            
            model = 'fer2013_mini_XCEPTION(rmsprop,acc).19-0.59.hdf5'
            
        
        elif red == 'Mini XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '100'  :
            
            AEN = 573
            FEN = 385
            
            AAS = 41
            FAS = 70
            
            AMI = 625
            FMI = 399
            
            AFE = 1413
            FFE = 361
            
            ATR = 824
            FTR = 423
            
            ASO = 611
            FSO = 220
            
            ANE = 403
            FNE = 830 

            model = 'fer2013_mini_XCEPTION(rmsprop,acc).56-0.63.hdf5'
            
#    BIG XCEPTION CNN -------------------------------------------------------------
        elif red == 'Big XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '25'  :
            
            AEN = 488
            FEN = 470
            
            AAS = 35
            FAS = 76
            
            AMI = 491
            FMI = 533
            
            AFE = 1005
            FFE = 769
            
            ATR = 630
            FTR = 602
            
            ASO = 357
            FSO = 474
            
            ANE = 271
            FNE = 962
            
            model = 'fer2013_big_XCEPTION.03-0.46.hdf5'
            
            
        elif red == 'Big XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '50'  :
            
            AEN = 658
            FEN = 308
            
            AAS = 38
            FAS = 73
            
            AMI = 633
            FMI = 391
            
            AFE = 1311
            FFE = 463
            
            ATR = 670
            FTR = 577
            
            ASO = 466
            FSO = 365
            
            ANE = 409
            FNE = 824
            
            model = 'fer2013_big_XCEPTION.24-0.57.hdf5'
            
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '100'  :
            
            AEN = 702
            FEN = 256
            
            AAS = 45
            FAS = 66
            
            AMI = 799
            FMI = 225
            
            AFE = 1377
            FFE = 397
            
            ATR = 881
            FTR = 366
            
            ASO = 641
            FSO = 190
            
            ANE = 395
            FNE = 838
         
            model = 'fer2013_big_XCEPTION.58-0.66.hdf5'
            
         
        elif red == 'Big XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '25'  :
            
            AEN = 315
            FEN = 643
            
            AAS = 2
            FAS = 109
            
            AMI = 358
            FMI = 666
            
            AFE = 793
            FFE = 981
            
            ATR = 449
            FTR = 801
            
            ASO = 267
            FSO = 564
            
            ANE = 120
            FNE = 1113
            
            model = 'fer2013_big_XCEPTION(sgd,mse,acc).06-0.32.hdf5'
            
            
        elif red == 'Big XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '50'  :
            
            AEN = 632
            FEN = 326
            
            AAS = 16
            FAS = 95
            
            AMI = 684
            FMI = 340
            
            AFE = 998
            FFE = 776
            
            ATR = 661
            FTR = 586
            
            ASO = 321
            FSO = 510
            
            ANE = 254
            FNE = 979
            
            model = 'fer2013_bigi_XCEPTION(rmsprop,acc).20-0.49.hdf5'
            
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '100'  :
            
            AEN = 721
            FEN = 237
            
            AAS = 32
            FAS = 95
            
            AMI = 684
            FMI = 340
            
            AFE = 1254
            FFE = 520
            
            ATR = 740
            FTR = 507
            
            ASO = 347
            FSO = 484
            
            ANE = 277
            FNE = 956
            
            model = 'fer2013_big_XCEPTION.24-0.57.hdf5'
            
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '25'  :
            
            AEN = 369
            FEN = 589
            
            AAS = 5
            FAS = 106
            
            AMI = 330
            FMI = 694
            
            AFE = 963
            FFE = 811
            
            ATR = 620
            FTR = 627
            
            ASO = 342
            FSO = 489
            
            ANE = 162
            FNE = 1071
            
            model = 'fer2013_big_XCEPTION(rmsprop,acc).04-0.38.hdf5'
            
            
        elif red == 'Big XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '50'  :
            
            AEN = 508
            FEN = 450
            
            AAS = 17
            FAS = 94
            
            AMI = 627
            FMI = 397
            
            AFE = 1092
            FFE = 682
            
            ATR = 726
            FTR = 521
            
            ASO = 433
            FSO = 398
            
            ANE = 211
            FNE = 1022
            
            model = 'fer2013_big_XCEPTION(rmsprop,acc).09-0.50.hdf5'
            
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '100'  :
            
            AEN = 702
            FEN = 25 
            
            AAS = 23
            FAS = 88
            
            AMI = 755
            FMI = 269
            
            AFE = 1199
            FFE = 575
            
            ATR = 688
            FTR = 559
            
            ASO = 594
            FSO = 237
            
            ANE = 283
            FNE = 950
            
            model = 'fer2013_big_XCEPTION(rmsprop,acc).30-0.58.hdf5'
            
        
        else :
            print('PARAMETRO NULO 1')
# GENERO ---------------------------------------------------------------------------   
    elif sentgen == 'Genero':
#        SIMPLE CNN ---------------------------------------------------------------
        if red == 'Simple CNN' and optimizador == 'Adam' and iteracciones == '25'  :
            
            AMA = 8100
            FMA = 1543
            
            AFEM = 8066
            FFEM = 997
            
            model = 'gender_Simple_CNN.01-0.86(adam).hdf5'
           
            
        elif red == 'Simple CNN' and optimizador == 'Adam' and iteracciones == '50'  :
            
            AMA = 8758
            FMA = 885
            
            AFEM = 8541
            FFEM= 522
            
            model = 'gender_Simple_CNN.04-0.93(adam).hdf5'
           
        
        elif red == 'Simple CNN' and optimizador == 'Adam' and iteracciones == '100'  :
            
            AMA = 8971
            FMA = 672
            
            AFEM = 9021
            FFEM = 42
           
            model = 'simple_CNN.81-0.96.hdf5'
         
        elif red == 'Simple CNN' and optimizador == 'SGD' and iteracciones == '25'  :
            
            AMA = 7428
            FMA = 2215
            
            AFEM = 7964
            FFEM = 1099
           
            model = 'gender_Simple_CNN.01-0.82(sgd).hdf5'
            
        elif red == 'Simple CNN' and optimizador == 'SGD' and iteracciones == '50'  :
            
            AMA = 7775
            FMA = 1868
            
            AFEM = 8147
            FFEM = 916
            
            model = 'gender_Simple_CNN.02-0.85(sgd).hdf5'
        
        elif red == 'Simple CNN' and optimizador == 'SGD' and iteracciones == '100'  :
            
            AMA = 8422
            FMA = 1221
            
            AFEM = 8597
            FFEM = 466
           
            model = 'gender_Simple_CNN.04-0.91(sgd).hdf5'
        
        elif red == 'Simple CNN' and optimizador == 'RMSprop' and iteracciones == '25'  :
            
            AMA = 8346
            FMA = 1297
            
            AFEM = 8269
            FFEM = 794
           
            model = 'gender_Simple_CNN.01-0.89(rmsprop).hdf5'
            
        elif red == 'Simple CNN' and optimizador == 'RMSprop' and iteracciones == '50'  :
            
            AMA = 8657
            FMA = 1086
            
            AFEM = 8861
            FFEM = 202
           
            model = 'gender_Simple_CNN.07-0.93(rmsprop).hdf5'
      
        
        elif red == 'Simple CNN' and optimizador == 'RMSprop' and iteracciones == '100'  :
            
            AMA = 8786
            FMA = 857
            
            AFEM = 8993
            FFEM = 70
           
            model = 'gender_Simple_CNN.14-0.95(rmsprop).hdf5'
            
            
#        MINI XCEPTION CNN -----------------------------------------------------------------
        elif red == 'Mini XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '25'  :
            
            AMA = 8321
            FMA = 1322
            
            AFEM = 8888
            FFEM = 175
           
            model = 'gender_mini_XCEPTION.01-0.92.hdf5'
            
            
        elif red == 'Mini XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '50'  :
            
            AMA = 8323
            FMA = 1320
            
            AFEM = 8888
            FFEM = 175
           
            model = 'gender_mini_XCEPTION.02-0.94.hdf5'
            
        
        elif red == 'Mini XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '100'  :
            
            AMA = 8783
            FMA = 860
            
            AFEM = 8988
            FFEM = 75 
            
            model = 'gender_mini_XCEPTION.21-0.95.hdf5'

         
        elif red == 'Mini XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '25'  :
            
            AMA = 8300
            FMA = 1334
            
            AFEM = 8466
            FFEM = 597
            
            model = 'gender_mini_XCEPTION.01-0.89(sgd).hdf'
                      
        elif red == 'Mini XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '50'  :
            
            AMA = 8701
            FMA = 942
            
            AFEM = 8746
            FFEM = 317
           
            model = 'gender_mini_XCEPTION.03-0.93(sgd).hdf5'
        
        elif red == 'Mini XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '100'  :
            
            AMA = 8798
            FMA = 845
            
            AFEM = 8841
            FFEM = 222
           
            model = 'gender_mini_XCEPTION.06-0.94(sgd).hdf5'
          
        
        elif red == 'Mini XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '25'  :
            
            AMA = 8146
            FMA = 1297
            
            AFEM = 8769
            FFEM = 294
           
            model = 'gender_mini_XCEPTION.01-0.90(rmsprop).hdf5'
            
            
        elif red == 'Mini XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '50'  :
            
            AMA = 8431
            FMA = 1212
            
            AFEM = 9011
            FFEM = 52
            
            model = 'gender_mini_XCEPTION.02-0.93(rmsprop).hdf5'
           
        
        elif red == 'Mini XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '100'  :
            
            AMA = 8843
            FMA = 800
            
            AFEM = 9015
            FFEM = 48 
           
            model = 'gender_mini_XCEPTION.08-0.95(rmsprop).hdf5'
           
#        BIG XCEPTION CNN-------------------------------------------------------------------
        elif red == 'Big XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '25'  :
            
            AMA = 8346
            FMA = 1297
            
            AFEM = 8481
            FFEM = 582
           
            model = 'gender_big_XCEPTION.01-0.90.hdf5'
           
            
        elif red == 'Big XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '50'  :
            
            AMA = 8657
            FMA = 1086
            
            AFEM = 8861
            FFEM = 202
           
            model = 'gender_big_XCEPTION.03-0.93.hdf5'
           
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'Adam' and iteracciones == '100'  :
            
            AMA = 8788
            FMA = 855
            
            AFEM = 8998
            FFEM = 65 
           
            model = 'gender_big_XCEPTION.06-0.95.hdf5'
            
         
        elif red == 'Big XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '25'  :
            
            AMA = 7328
            FMA = 2315
            
            AFEM = 7961
            FFEM = 1102
           
            model = 'gender_big_XCEPTION.01-0.81(sgd).hdf5'
            
            
        elif red == 'Big XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '50'  :
            
            AMA = 8228
            FMA = 1415
            
            AFEM = 8461
            FFEM = 602
            
            model = 'gender_big_XCEPTION.02-0.89(sgd).hdf5'
            
         
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'SGD' and iteracciones == '100'  :
            
            AMA = 8629
            FMA = 1014
            
            AFEM = 8871
            FFEM = 192 
            
            model = 'gender_big_XCEPTION.05-0.93(sgd).hdf5'
           
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '25'  :
            
            AMA = 7779
            FMA = 1865
            
            AFEM = 8158
            FFEM = 905
            
            model = 'gender_big_XCEPTION.01-0.85(rmsprop).hdf5'
            
        elif red == 'Big XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '50'  :
            
            AMA = 8544
            FMA = 1099
            
            AFEM = 8754
            FFEM = 309
           
            model = 'gender_big_XCEPTION.03-0.92(rmsprop).hdf5'
        
        elif red == 'Big XCEPTION CNN' and optimizador == 'RMSprop' and iteracciones == '100'  :
            
            AMA = 8666
            FMA = 977
            
            AFEM = 8944
            FFEM = 119
            
            model = 'gender_big_XCEPTION.05-0.94(rmsprop).hdf5'
        
        else :
            print('PARAMETRO NULO 2')
    else :
        
        print('PARAMETRO NULO 3')
                 
    return int(AEN),int(FEN),int(AAS),int(FAS),int(AMI),int(FMI),int(AFE),int(FFE),int(ATR),int(FTR),int(ASO),int(FSO),int(ANE),int(FNE),int(AMA),int(FMA),int(AFEM),int(FFEM),model

def desgeneraliza(emotion_text):
    
    result = ''
    
    if(emotion_text == 'Enfadado'):
        result = 'Enfado'
    elif(emotion_text == 'Sorprendido'):
        result = 'Sorpresa'
    elif(emotion_text == 'Miedoso'):
        result = 'Miedo'
    elif(emotion_text == 'Asqueado'):
        result = 'Asco'
    elif(emotion_text == 'Feliz'):
        result = 'Felicidad'
    elif(emotion_text == 'Triste'):
        result = 'Tristeza'
    else:
        result = emotion_text
    return result

def demostracion(pathfile, model, pathmodel, sentgen):
    
    emotion_text=''
    gender_text=''
    
    print(BASE_DIR_RE)
    print(BASE_DIR_RE+pathmodel+model)
    
    # parametros cargar imagenes dataset
    image_path =BASE_DIR_RE+pathfile
    detection_model_path = BASE_DIR_RE+'/image/trained_models/detection_models/haarcascade_frontalface_default.xml'
    emotion_model_path = BASE_DIR_RE+pathmodel+model
    gender_model_path = BASE_DIR_RE+'/image/trained_models/gender_models/simple_CNN.81-0.96.hdf5'
    emotion_labels = get_labels('fer2013')
    gender_labels = get_labels('imdb')
    font = cv2.FONT_HERSHEY_SIMPLEX
        
    # dimensiones boundbox
    gender_offsets = (30, 60)
    gender_offsets = (10, 10)
    emotion_offsets = (20, 40)
    emotion_offsets = (0, 0)
        
    # carga de los modelos
    face_detection = load_detection_model(detection_model_path)
    
    emotion_classifier = load_model(emotion_model_path, compile=False)
    gender_classifier = load_model(gender_model_path, compile=False)
        
    # getting input model shapes for inference
    emotion_target_size = emotion_classifier.input_shape[1:3]
    gender_target_size = gender_classifier.input_shape[1:3]
        
    # carga de imagenes
    rgb_image = load_image(image_path, grayscale=False)
    gray_image = load_image(image_path, grayscale=True)
    gray_image = np.squeeze(gray_image)
    gray_image = gray_image.astype('uint8')
      
    faces = detect_faces(face_detection, gray_image)
    for face_coordinates in faces:
        x1, x2, y1, y2 = apply_offsets(face_coordinates, gender_offsets)
        rgb_face = rgb_image[y1:y2, x1:x2]
        
        x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
        gray_face = gray_image[y1:y2, x1:x2]
        
        try:
            rgb_face = cv2.resize(rgb_face, (gender_target_size))
            gray_face = cv2.resize(gray_face, (emotion_target_size))
        except:
            continue
        
    # prediccion del genero
        rgb_face = preprocess_input(rgb_face, False)
        rgb_face = np.expand_dims(rgb_face, 0)
        gender_prediction = gender_classifier.predict(rgb_face)
        gender_label_arg = np.argmax(gender_prediction)
        gender_text = gender_labels[gender_label_arg]
        
    # prediccion de la emocion
        gray_face = preprocess_input(gray_face, True)
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)
        emotion_label_arg = np.argmax(emotion_classifier.predict(gray_face))
        emotion_text = emotion_labels[emotion_label_arg]
        
        if gender_text == gender_labels[0]:
            color = (0, 0, 255)
        else:
            color = (255, 0, 0)
            
        # marco resultado
        draw_bounding_box(face_coordinates, rgb_image, color)
        #draw_text(face_coordinates, rgb_image, gender_text, color, 0, 90, 0.6, 2)
        #draw_text(face_coordinates, rgb_image, emotion_text, color, 0, 120, 0.6, 2)
    
    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(BASE_DIR_RE+'/media/prediccion.png', bgr_image)
    
        
    return emotion_text, gender_text
