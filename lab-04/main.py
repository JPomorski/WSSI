import matplotlib.pyplot as plt
import numpy as np
from layer import Layer
from network import Network

fig, ax = plt.subplots()

layer = Layer(3, 2)
print(layer.get_values(np.array([0.0, 0.1])))

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
            ax.text((x - radius) - 0.02, y, 'input', ha='right', va='center')
            if j == size - 1:
                ax.text(x, -0.1, 'input\nlayer', weight='bold', ha='center')
        if i == n_layers - 1:   # and the output as well
            neuron.set_facecolor('#76f249')
            ax.text((x + radius) + 0.02, y, 'output', ha='left', va='center')
            if j == size - 1:
                ax.text(x, -0.1, 'output\nlayer', weight='bold', ha='center')

    neuron_positions.append(layer_neuron_positions)

# drawing edges
for i in range(len(neuron_positions) - 1):
    for (x1, y1) in neuron_positions[i]:
        for (x2, y2) in neuron_positions[i + 1]:
            ax.plot([x1, x2], [y1, y2], 'k:', zorder=1)

# ax.add_patch(plt.Circle((.5, .5), 0.1, color='blue', zorder=2))

ax.axis('off')
plt.show()

test_data = np.random.rand(1000, 2)
# print(test_data[0:5, :])
