import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time

def init_params():
    W1 = np.random.rand(10, 784) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def sigmoid(x) :
    return 1/ (1 + np.exp(-x))

def tanh(x) :
    return np.tanh(x)

def leaky_relu(x, alpha=0.01) :
    return np.where(x> 0, x, alpha * x)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A
    
def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    A1 = leaky_relu(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def ReLU_deriv(Z):
    return Z > 0

def sigmoid_deriv(x) :
    s = sigmoid(x)
    return s* (1-s)

def tanh_deriv(x) :
    return 1-np.tanh(x)**2

def leaky_relu_deriv(x, alpha=0.01):
    return np.where(x>0 , 1, alpha)

def softmax_deriv(x) :
    s = softmax(x).reshape(-1,1)
    return np.diagflat(s) - np.dot(s,s.T)

def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max() + 1))
    one_hot_Y[np.arange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y

def backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y):
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dW2 = 1 / m * dZ2.dot(A1.T)
    db2 = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * leaky_relu_deriv(Z1)
    dW1 = 1 / m * dZ1.dot(X.T)
    db1 = 1 / m * np.sum(dZ1)
    return dW1, db1, dW2, db2

def update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha):
    W1 = W1 - alpha * dW1
    b1 = b1 - alpha * db1    
    W2 = W2 - alpha * dW2  
    b2 = b2 - alpha * db2    
    return W1, b1, W2, b2

def get_predictions(A2):
    return np.argmax(A2, 0)

def get_accuracy(predictions, Y):
    print(predictions, Y)
    return np.sum(predictions == Y) / Y.size


# def gradient_descent(X, Y, alpha, iterations):
#     W1, b1, W2, b2 = init_params()
#     for i in range(iterations):
#         Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
#         dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
#         W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
#         if i % 10 == 0:
#             print("Iteration: ", i)
#             predictions = get_predictions(A2)
#             print(get_accuracy(predictions, Y))
#     return W1, b1, W2, b2

def gradient_descent(X, Y, alpha, iterations):
    W1, b1, W2, b2 = init_params()
    accuracy_list = []
    iteration_list = []
    
    for i in range(iterations):
        Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
        dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
        W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
        predictions = get_predictions(A2)
        accuracy = get_accuracy(predictions, Y)
        loss = mean_absolute_error(Y,predictions)
        if loss <= 0.1 :
            print(f"Iteration: {i}")
            break
        if i % 10 == 0:
            accuracy_list.append(accuracy)
            iteration_list.append(i)
            print(f'loss : {loss}')
            print(f"Iteration: {i}, Accuracy: {accuracy}")
    
    # Plot accuracy over iterations
    plt.plot(iteration_list, accuracy_list)
    plt.title("Accuracy over Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Accuracy")
    plt.grid()
    plt.show()

    
    return W1, b1, W2, b2

def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    return predictions

def mean_absolute_error(act, pred):
    diff = pred - act
    abs_diff = np.absolute(diff)
    mean_diff = abs_diff.mean()
    return mean_diff

def test_prediction(index, W1, b1, W2, b2):
    current_image = X_train[:, index, None]
    prediction = make_predictions(X_train[:, index, None], W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
    
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()

def test_all(W1, b1, W2, b2):
    fig,ax = plt.subplots(10,10,
                      figsize = (10,10),
                      subplot_kw= {'xticks':[],'yticks':[]},
                      gridspec_kw=dict(hspace = 0.1,wspace = 0.1))
    for i ,axi in enumerate(ax.flat):
        current_image = X_train[:, i, None]
        prediction = make_predictions(X_train[:, i, None], W1, b1, W2, b2)
        label = Y_train[i]
        axi.imshow(current_image.reshape(28,28),cmap='gray',interpolation='nearest')
        axi.text(0.05,0.05,str(label),transform = axi.transAxes,color = "yellow")
        axi.text(0.75,0.05,str(prediction),transform = axi.transAxes,color = "green" if prediction == label else "red")
    plt.show()

data = pd.read_csv(r'semester 2\train.csv')

data = np.array(data)
m, n = data.shape
np.random.shuffle(data) # shuffle before splitting into dev and training sets

data_dev = data[0:1000].T
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
X_dev = X_dev / 255.

data_train = data[1000:m].T
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.
_,m_train = X_train.shape

start = time.time()

W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 0.50, 1000)



test_all(W1, b1, W2, b2)
# test_prediction(5, W1, b1, W2, b2)
# test_prediction(4, W1, b1, W2, b2)
# test_prediction(7, W1, b1, W2, b2)
# test_prediction(9, W1, b1, W2, b2)

dev_predictions = make_predictions(X_dev, W1, b1, W2, b2)

end = time.time()

get_accuracy(dev_predictions, Y_dev)

print(end-start)