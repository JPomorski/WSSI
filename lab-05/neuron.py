import numpy as np


class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.inputs = None
        self.output_value = None
        self.calc_value = None

        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

        # print(n_inputs)

    @staticmethod
    def _f(x):  # activation function (here: leaky_relu)
        return max(x * .1, x)

    def fw_pass(self, xs):  # calculate the neuron's output: multiply the inputs with the weights
        # and sum the values together, add the bias value,
        # then transform the value via an activation function
        self.inputs = xs
        self.calc_value = xs @ self.ws
        self.output_value = self._f(self.calc_value)
        return self.output_value
