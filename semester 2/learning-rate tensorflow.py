import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.api.models import Sequential
from keras.api.layers import Dense, Flatten
from keras.api.optimizers import Adam
def load_data():
    data = pd.read_csv('semester 2/train.csv')
    data = np.array(data)
    np.random.shuffle(data)  # Shuffle the data
    m, n = data.shape
    data_dev = data[:1000]
    data_train = data[1000:]
    X_dev, Y_dev = data_dev[:, 1:] / 255.0, data_dev[:, 0]
    X_train, Y_train = data_train[:, 1:] / 255.0, data_train[:, 0]
    return X_train, Y_train, X_dev, Y_dev

def build_model():
    model = Sequential([
        Flatten(input_shape=(784,)),  # Input layer (28x28 flattened)
        Dense(100, activation='relu'),  # First hidden layer
        Dense(40, activation='relu'),   # Second hidden layer
        Dense(10, activation='softmax') # Output layer
    ])
    return model

def compile_and_train(model, X_train, Y_train, X_dev, Y_dev, alpha, epochs):
    model.compile(optimizer=Adam(learning_rate=alpha),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    history = model.fit(X_train, Y_train, epochs=epochs, batch_size=32, validation_data=(X_dev, Y_dev))
    return history

def plot_accuracy(history):
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid()
    plt.show()

def evaluate_model(model, X_dev, Y_dev):
    loss, accuracy = model.evaluate(X_dev, Y_dev)
    print(f"Validation Set Accuracy: {accuracy:.4f}")

def main():
    X_train, Y_train, X_dev, Y_dev = load_data()
    model = build_model()
    history = compile_and_train(model, X_train, Y_train, X_dev, Y_dev, alpha=2e-5, epochs=20)
    plot_accuracy(history)
    evaluate_model(model, X_dev, Y_dev)

if __name__ == "__main__":
    main()
