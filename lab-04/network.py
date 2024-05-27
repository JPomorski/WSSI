from layer import Layer


class Network:
    def __init__(self, n_layers, layer_sizes):
        self.layers = []
        self.layers.append(Layer(layer_sizes[0], 1))

        for i in range(1, n_layers):
            self.layers.append(Layer(layer_sizes[i], layer_sizes[i - 1]))
        print(self.layers)
