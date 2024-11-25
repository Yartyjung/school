import numpy as np
import pandas as pd
import time
from matplotlib import pyplot as plt
 
def init_params():
    n1 = 100  # First hidden layer size
    n2 = 40  # Second hidden layer size
    n3 = 10  # Third hidden layer size (new layer)
    W1 = np.random.rand(n1, 784) - 0.5
    b1 = np.random.rand(n1, 1) - 0.5
    W2 = np.random.rand(n2, n1) - 0.5
    b2 = np.random.rand(n2, 1) - 0.5
    W3 = np.random.rand(n3, n2) - 0.5  # New layer parameters
    b3 = np.random.rand(n3, 1) - 0.5
    return W1, b1, W2, b2, W3, b3
 
def ReLU(Z):
    return np.maximum(Z, 0)
 
def softmax(Z):
    A = np.exp(Z) / np.sum(np.exp(Z), axis=0)
    return A
   
def forward_prop(W1, b1, W2, b2, W3, b3, X):
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = ReLU(Z2)
    Z3 = W3.dot(A2) + b3  # New layer forward pass
    A3 = softmax(Z3)
    return Z1, A1, Z2, A2, Z3, A3
 
def ReLU_deriv(Z):
    return Z > 0
 
def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y
 
def backward_prop(Z1, A1, Z2, A2, Z3, A3, W1, W2, W3, X, Y):
    one_hot_Y = one_hot(Y)
    dZ3 = A3 - one_hot_Y
    dW3 = 1 / m * dZ3.dot(A2.T)
    db3 = 1 / m * np.sum(dZ3, axis=1, keepdims=True)
    dZ2 = W3.T.dot(dZ3) * ReLU_deriv(Z2)
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1, axis=1, keepdims=True)
    return dW1, db1, dW2, db2, dW3, db3
 
def update_params(W1, b1, W2, b2, W3, b3, dW1, db1, dW2, db2, dW3, db3, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1    
    W2 = W2 - alpha * dW2  
    b2 = b2 - alpha * db2    
    W3 = W3 - alpha * dW3  # Update new layer weights and biases
    b3 = b3 - alpha * db3    
    return W1, b1, W2, b2, W3, b3
 
def get_predictions(A3):
    return np.argmax(A3, 0)
 
def get_accuracy(predictions, Y):
    return np.sum(predictions == Y) / Y.size
 
def gradient_descent(X, Y, alpha, iterations):
    W1, b1, W2, b2, W3, b3 = init_params()
    accuracy_list = []
    iteration_list = []
   
    for i in range(iterations):
        Z1, A1, Z2, A2, Z3, A3 = forward_prop(W1, b1, W2, b2, W3, b3, X)
        dW1, db1, dW2, db2, dW3, db3 = backward_prop(Z1, A1, Z2, A2, Z3, A3, W1, W2, W3, X, Y)
        W1, b1, W2, b2, W3, b3 = update_params(W1, b1, W2, b2, W3, b3, dW1, db1, dW2, db2, dW3, db3, alpha)
       
        if i % 10 == 0:
            predictions = get_predictions(A3)
            accuracy = get_accuracy(predictions, Y)
            accuracy_list.append(accuracy)
            iteration_list.append(i)
            print(f"Iteration: {i}, Accuracy: {accuracy}")
   
    # Plot accuracy over iterations
    plt.plot(iteration_list, accuracy_list)
    plt.title("Accuracy over Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Accuracy")
    plt.grid()
    plt.show()
   
    return W1, b1, W2, b2, W3, b3
 
def make_predictions(X, W1, b1, W2, b2, W3, b3):
    _, _, _, _, _, A3 = forward_prop(W1, b1, W2, b2, W3, b3, X)
    predictions = get_predictions(A3)
    return predictions
 
def test_prediction(index, W1, b1, W2, b2, W3, b3):
    current_image = X_train[:, index, None]
    prediction = make_predictions(X_train[:, index, None], W1, b1, W2, b2, W3, b3)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
   
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()
 
def test_all(W1, b1, W2, b2, W3, b3):
    fig, ax = plt.subplots(10, 10, figsize=(10, 10),
                           subplot_kw={'xticks': [], 'yticks': []},
                           gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, axi in enumerate(ax.flat):
        current_image = X_train[:, i, None]
        prediction = make_predictions(X_train[:, i, None], W1, b1, W2, b2, W3, b3)
        label = Y_train[i]
        axi.imshow(current_image.reshape(28, 28), cmap='gray', interpolation='nearest')
        axi.text(0.05, 0.05, str(label), transform=axi.transAxes, color="yellow")
        axi.text(0.75, 0.05, str(prediction), transform=axi.transAxes, color="green" if prediction == label else "red")
    end = time.time()
    print(f"Training Time: {end - start} seconds")
   
    plt.show()
 
data = pd.read_csv('semester 2/train.csv')
 
data = np.array(data)
m, n = data.shape
np.random.shuffle(data)  # shuffle before splitting into dev and training sets
 
data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.
 
data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_, m_train = X_train.shape
 
start = time.time()
 
W1, b1, W2, b2, W3, b3 = gradient_descent(X_train, Y_train, 0.2, 1000)
 
test_all(W1, b1, W2, b2, W3, b3)
# test_prediction(5, W1, b1, W2, b2, W3, b3)
# test_prediction(4, W1, b1, W2, b2, W3, b3)
# test_prediction(7, W1, b1, W2, b2, W3, b3)
# test_prediction(9, W1, b1, W2, b2, W3, b3)
 
dev_predictions = make_predictions(X_dev, W1, b1, W2, b2, W3, b3)
 
 
accuracy = get_accuracy(dev_predictions, Y_dev)
print(f"Development Set Accuracy: {accuracy}")