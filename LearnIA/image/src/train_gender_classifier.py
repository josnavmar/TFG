from keras.callbacks import CSVLogger, ModelCheckpoint, EarlyStopping
from keras.callbacks import ReduceLROnPlateau
from image.src.utils.datasets import DataManager
from image.src.models.cnn import simple_CNN
from image.src.utils.data_augmentation import ImageGenerator
from image.src.utils.datasets import split_imdb_data

# parametros
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
images_path = '../datasets/imdb_crop/imdb_crop/'
log_file_path = '../trained_models/gender_models/gender_training.log'
trained_models_path = '../trained_models/gender_models/gender_Simple_CNN'

# carga dataset
data_loader = DataManager(dataset_name)
ground_truth_data = data_loader.get_data()
train_keys, val_keys = split_imdb_data(ground_truth_data, validation_split)
print('Numero de muestras de entrenamiento:', len(train_keys))
print('Numero de muestras de validacion:', len(val_keys))
image_generator = ImageGenerator(ground_truth_data, batch_size,
                                 input_shape[:2],
                                 train_keys, val_keys, None,
                                 path_prefix=images_path,
                                 vertical_flip_probability=0,
                                 grayscale=grayscale,
                                 do_random_crop=do_random_crop)

# model parameters/compilation
model = simple_CNN(input_shape, num_classes)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.summary()

# guarda modelo
early_stop = EarlyStopping('val_loss', patience=patience)
reduce_lr = ReduceLROnPlateau('val_loss', factor=0.1,
                              patience=int(patience/2), verbose=1)
csv_logger = CSVLogger(log_file_path, append=False)
model_names = trained_models_path + '.{epoch:02d}-{val_acc:.2f}(rmsprop).hdf5'
model_checkpoint = ModelCheckpoint(model_names,
                                   monitor='val_loss',
                                   verbose=1,
                                   save_best_only=True,
                                   save_weights_only=False)
callbacks = [model_checkpoint, csv_logger, early_stop, reduce_lr]

# entrenamiento model
model.fit_generator(image_generator.flow(mode='train'),
                    steps_per_epoch=int(len(train_keys) / batch_size),
                    epochs=num_epochs, verbose=1,
                    callbacks=callbacks,
                    validation_data=image_generator.flow('val'),
                    validation_steps=int(len(val_keys) / batch_size))

