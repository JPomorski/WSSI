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

vertical_space = 1.0 / max(layer_sizes)
horizontal_space = 1.0 / (n_layers - 1)

# drawing neurons
neuron_positions = []
for i, size in enumerate(layer_sizes):  # iterate over layers
    layer_neuron_positions = []
    for j in range(size):  # iterate over neurons
        x = i * horizontal_space
        y = (j - size / 2) * vertical_space + 0.5
        layer_neuron_positions.append((x, y))
        radius = 0.07
        neuron = plt.Circle((x, y),
                            radius,
                            facecolor='#508beb',
                            edgecolor='black',
                            linewidth=1,
                            zorder=2)
        ax.add_patch(neuron)

        if i == 0:  # coloring and marking the input layer
            neuron.set_facecolor('#f2ba49')
            ax.text((x - radius) - 0.04, y, 'input', ha='right', va='center')
            if j == 0:
                ax.text(x, -0.1, 'input\nlayer', weight='bold', ha='center')
                border = plt.Rectangle(((x - radius) - 0.02, 0), radius * 2 + 0.04,
                                       vertical_space * layer_sizes[0], color='#e3d9c1', zorder=0)
                ax.add_patch(border)

        if i == n_layers - 1:  # and the output as well
            neuron.set_facecolor('#76f249')
            ax.text((x + radius) + 0.04, y, 'output', ha='left', va='center')
            if j == 0:
                ax.text(x, -0.1, 'output\nlayer', weight='bold', ha='center')
                border = plt.Rectangle(((x - radius) - 0.02, 0), radius * 2 + 0.04,
                                       vertical_space * layer_sizes[0], color='#cde3c1', zorder=0)
                ax.add_patch(border)

    neuron_positions.append(layer_neuron_positions)

# drawing edges
for i in range(len(neuron_positions) - 1):
    for (x1, y1) in neuron_positions[i]:
        for (x2, y2) in neuron_positions[i + 1]:
            ax.plot([x1, x2], [y1, y2], 'k:', zorder=1)

# ax.add_patch(plt.Circle((.5, .5), 0.1, color='blue', zorder=2))

ax.axis('off')
plt.show()

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
