import sys

import cv2
from keras.models import load_model
import numpy as np
import itertools
import matplotlib.pyplot as plt
from matplotlib import cm

from image.src.utils.datasets import DataManager
from image.src.utils.datasets import split_data
from image.src.utils.preprocessor import preprocess_input
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from image.src.utils.datasets import split_imdb_data
from sklearn.metrics import confusion_matrix

#EMOTIONS
class_names_emotion = ["Enfadado", "Asqueado", "Miedoso", "Feliz", "Triste", "Sorprendido", "Neutral"]
emotion_model_path = '../trained_models/emotion_models/fer2013_simple_CNN(adam,acc).13-0.54.hdf5'
emotion_classifier = load_model(emotion_model_path, compile=False)
dataset_emotion = 'fer2013'
input_shape = (64, 64, 1)
validation_split = .2


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.get_cmap('Blues')):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


# Compute confusion matrix about emotions--------------------------------------------
    
data_loader = DataManager(dataset_emotion, image_size=input_shape[:2])
faces, emotions = data_loader.get_data()
faces = preprocess_input(faces)
num_samples, num_classes = emotions.shape
train_data, val_data = split_data(faces, emotions, validation_split)
train_faces, train_emotions = train_data
x_test, y_test = val_data

y_pred = emotion_classifier.predict(x_test)
#y_pred = y_pred > 0.5

cnf_matrix = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix about emotions
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names_emotion,
                     title='Confusion matrix about emotions, without normalization')

# Plot normalized confusion matrix about emotions
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names_emotion, normalize=True,
                     title='Normalized confusion matrix about emotions')


plt.show()

