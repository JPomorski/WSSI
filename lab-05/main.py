import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
# import seaborn as sns
from layer import Layer
from network import Network


# categorical cross-entropy for classification
def loss_function(predictions, targets):
    predictions = np.array(predictions)
    targets = np.array(targets)
    return -np.mean(targets * np.log(predictions + 1e-10))


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


fig, ax = plt.subplots()

layer = Layer(3, 2)
# print(layer.get_values(np.array([0.0, 0.1])))

layer_sizes = [3, 5, 2]
n_layers = len(layer_sizes)

network = Network(n_layers, layer_sizes)

# testing the network
n_epochs = 50
learning_rate = 0.01

np.random.seed(123)
test_data = np.random.rand(10, 3)
# print(test_data)

test_targets = [1 if x[0] + x[1] + x[2] <= 2 else 0 for x in test_data]
test_targets = np.eye(2)[test_targets]
# print(test_targets)

for epoch in range(n_epochs):
    epoch_loss = 0.0
    for input_data, target_data in zip(test_data, test_targets):
        test_predictions = softmax(network.calculate(input_data))

        loss = loss_function(test_predictions, target_data)
        epoch_loss += loss

        # print(test_predictions)
        # print(target_data)

        loss_gradients = test_predictions - target_data
        # print(loss_gradients)

        network.bw_pass(loss_gradients)
        network.update(learning_rate)

        # draw plot to visualise the data
        # prediction_x = test_predictions[0]
        # prediction_y = test_predictions[1]
        # ax.scatter(prediction_x, prediction_y, color='yellow', s=70, linewidth=2, edgecolor='k')
        # ax.scatter(target_data[0], target_data[1], color='gold', s=70, linewidth=2, edgecolor='k')

    print(epoch_loss)


# plt.legend(loc='upper right')
# plt.show()
