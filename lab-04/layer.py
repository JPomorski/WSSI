from neuron import Neuron


class Layer:
    def __init__(self, n_neurons, n_inputs, bias=0., weights=None):
        self.neuron_array = [Neuron(n_inputs, bias, weights) for _ in range(n_neurons)]
        # print(self.neuron_array)

    def get_values(self, inputs):
        return [neuron(inputs) for neuron in self.neuron_array]
