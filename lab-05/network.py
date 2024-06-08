from layer import Layer


class Network:
    def __init__(self, n_layers, layer_sizes, bias=0., weights=None):
        self.layers = []

        for i in range(1, n_layers):
            self.layers.append(Layer(layer_sizes[i], layer_sizes[i - 1], bias, weights))
        # print(self.layers)

    def calculate(self, inputs):
        for layer in self.layers:
            inputs = layer.get_values(inputs)
        return inputs

    def bw_pass(self, loss_gradients):
        gradient_inputs = loss_gradients
        for layer in reversed(self.layers):
            gradient_inputs = layer.bw_pass(gradient_inputs)
        return gradient_inputs

    def update(self, learning_rate):
        for layer in self.layers:
            for neuron in layer.neuron_array:
                neuron.ws -= learning_rate * neuron.gradient_ws
                neuron.b -= learning_rate * neuron.gradient_b
