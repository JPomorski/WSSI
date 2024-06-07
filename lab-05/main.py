import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from layer import Layer
from network import Network

fig, ax = plt.subplots()

layer = Layer(3, 2)
# print(layer.get_values(np.array([0.0, 0.1])))

layer_sizes = [3, 4, 4, 1]
n_layers = len(layer_sizes)

network = Network(n_layers, layer_sizes)

# testing the network
print(network.calculate(np.array([0.1, -0.3, 0.8])))

test_data = np.random.rand(1000, 3)
test_predictions = [network.calculate(test)[0] for test in test_data]

# print(test_data[0:5, :])
# print(test_predictions)

sns.scatterplot(x="x",
                y="y",
                hue="class",
                palette={"higher": "red", "lower": "#508beb"},
                data=pd.DataFrame({'x': [x for x, _, _ in test_data],
                                   'y': [y for _, y, _ in test_data],
                                   'z': [z for _, _, z in test_data],
                                   'class': ['higher' if p >= 2.6 else 'lower' for p in test_predictions]}))

plt.legend(loc='upper right')
plt.show()
