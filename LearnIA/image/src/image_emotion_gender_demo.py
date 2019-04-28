import sys

import cv2
from keras.models import load_model
import numpy as np

from image.src.utils.datasets import get_labels
from image.src.utils.inference import detect_faces
from image.src.utils.inference import draw_text
from image.src.utils.inference import draw_bounding_box
from image.src.utils.inference import apply_offsets
from image.src.utils.inference import load_detection_model
from image.src.utils.inference import load_image
from image.src.utils.preprocessor import preprocess_input

# parametros cargar imagenes dataset
image_path = '../images/triste2.jpg'
detection_model_path = 'C:/Users/JCRN/git/TFG/LearnIA/image/trained_models/detection_models/haarcascade_frontalface_default.xml'
emotion_model_path = 'C:/Users/JCRN/git/TFG/LearnIA/image/trained_models/emotion_models/fer2013_big_XCEPTION.58-0.66.hdf5'
gender_model_path = 'C:/Users/JCRN/git/TFG/LearnIA/image/trained_models/gender_mini_XCEPTION.02-0.93(rmsprop).hdf5'
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
    draw_text(face_coordinates, rgb_image, gender_text, color, 0, 90, 0.6, 2)
    draw_text(face_coordinates, rgb_image, emotion_text, color, 0, 120, 0.6, 2)

bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('../images/prediccion.png', bgr_image)
