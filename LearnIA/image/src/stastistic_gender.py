import sys

import cv2
from keras.models import load_model
import numpy as np
import itertools
import matplotlib.pyplot as plt

from image.src.utils.datasets import DataManager
from image.src.utils.datasets import split_data
from image.src.utils.preprocessor import preprocess_input
from image.src.utils.data_augmentation import ImageGenerator
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from image.src.utils.datasets import split_imdb_data
from sklearn.metrics import confusion_matrix

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

#GENDER
class_names_gender = ["Mujer", "Hombre"]
batch_size = 32
num_epochs = 1000
validation_split = .2
do_random_crop = False
patience = 100
num_classes = 2
dataset_name = 'imdb'
input_shape = (64, 64, 1)
if input_shape[2] == 1:
    grayscale = True
images_path = '../datasets/imdb_crop/'
log_file_path = '../trained_models/gender_models/gender_training.log'
trained_models_path = '../trained_models/gender_models/gender_mini_XCEPTION'
gender_model_path ='../trained_models/gender_models/simple_CNN.81-0.96.hdf5'

# carga dataset
data_loader = DataManager(dataset_name)
ground_truth_data = data_loader.get_data()
train_keys, val_keys = split_imdb_data(ground_truth_data, validation_split)
print('Numero de muestras de entrenamiento:', len(train_keys))
print('Numero de muestras de validacion:', len(val_keys))
print(train_keys)
datagen = ImageGenerator(ground_truth_data, batch_size,
                                 input_shape[:2],
                                 train_keys, val_keys, None,
                                 path_prefix=images_path,
                                 vertical_flip_probability=0,
                                 grayscale=grayscale,
                                 do_random_crop=do_random_crop)

test_generator = datagen.flow('val')
'''
x_test, y_test = regression_flow_from_directory(test_generator)

gender_classifier = load_model(gender_model_path, compile=False)

pred=gender_classifier.predict_generator(x_test, steps=batch_size)

predicted_class_indices=np.argmax(pred,axis=1)



# Compute confusion matrix about gender--------------------------------------------
    
cnf_matrix = confusion_matrix(test_generator.classes, predicted_class_indices,class_names_gender)

np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix about gender
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names_gender,
                      title='Confusion matrix about gender, without normalization')

# Plot normalized confusion matrix about gender
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names_gender, normalize=True,
                      title='Normalized confusion matrix about gender')

plt.show()

#Evaluating using Keras model_evaluate:
x, y = zip(*(test_generator[i] for i in range(len(test_generator))))
x_test, y_test = np.vstack(x), np.vstack(y)
loss, acc = gender_classifier.evaluate(x_test, y_test, batch_size=64)

print("Accuracy: " ,acc)
print("Loss: ", loss)

'''