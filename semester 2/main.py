#image size 100x100

import tensorflow as tf 
import keras
from keras.api.preprocessing import image_dataset_from_directory 
from keras.api.models import Sequential
from keras.api.layers import Conv2D ,Dense ,Flatten ,MaxPooling2D, Rescaling, InputLayer
import matplotlib.pyplot as plt

train = image_dataset_from_directory("/Users/nattapat.ems/Desktop/school/Semester 2/Fruit classification/archive/train/train" ,batch_size=32, image_size=(100, 100), validation_split=0.3, subset="training", seed=123)
val = image_dataset_from_directory("/Users/nattapat.ems/Desktop/school/Semester 2/Fruit classification/archive/train/train" ,batch_size=32, image_size=(100, 100), validation_split=0.3, subset="validation", seed=123)

print(train.class_names)

imageHeight = 100
imageWidth = 100
thickness = 3
inputShape = (imageHeight, imageWidth, thickness)

model = Sequential()

model.add(InputLayer(shape=inputShape,batch_size=32))
model.add(Conv2D(64, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D((2, 2)))


model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dense(33, activation="softmax"))


model.compile(optimizer=keras.optimizers.Adam(1e-5), loss=keras.losses.SparseCategoricalCrossentropy(), metrics=["accuracy"])

model.summary()

epoch = 5
history = model.fit(train, validation_data=val, epochs=epoch)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epoch)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open('/Users/nattapat.ems/Desktop/school/Semester 2/Fruit classification/model.tflite', 'wb') as f:
  f.write(tflite_model)