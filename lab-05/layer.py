from neuron import Neuron


class Layer:
    def __init__(self, n_neurons, n_inputs, bias=0., weights=None):
        self.neuron_array = [Neuron(n_inputs, bias, weights) for _ in range(n_neurons)]
        # print(self.neuron_array)

    def get_values(self, inputs):
        return [neuron.fw_pass(inputs) for neuron in self.neuron_array]

    def bw_pass(self, loss_gradients):
        gradient_inputs = []
        for neuron, gradient in zip(self.neuron_array, loss_gradients):
            gradient_inputs.append(neuron.bw_pass(gradient))
        return gradient_inputs
