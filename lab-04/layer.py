from neuron import Neuron


class Layer:
    def __init__(self, n_neurons, n_inputs):
        self.neuron_array = [Neuron(n_inputs) for _ in range(n_neurons)]
        print(self.neuron_array)

    def get_values(self, inputs):
        return [neuron(inputs) for neuron in self.neuron_array]
