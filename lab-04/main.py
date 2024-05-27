import matplotlib.pyplot as plt
import numpy as np
from layer import Layer
from network import Network


def visualise():
    fig, ax = plt.subplots()


layer = Layer(3, 2)
print(layer.get_values(np.array([0.0, 0.1])))

layer_sizes = [3, 4, 4, 1]
network = Network(4, layer_sizes)

test_data = np.random.rand(1000, 2)
# print(test_data[0:5, :])
