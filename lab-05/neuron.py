import numpy as np


class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

        self.inputs = None
        self.output_value = None
        self.calc_value = None

        self.gradient_ws = None
        self.gradient_b = None
        self.gradient_inputs = None

        # print(n_inputs)

    @staticmethod
    def _f(x):  # activation function (here: leaky_relu)
        return max(x * .1, x)

    @staticmethod
    def _f_derivative(x):
        return np.where(x > 0, 1, 0.1)

    def fw_pass(self, xs):  # calculate the neuron's output: multiply the inputs with the weights
        # and sum the values together, add the bias value,
        # then transform the value via an activation function
        self.inputs = xs
        self.calc_value = xs @ self.ws
        self.output_value = self._f(self.calc_value)
        return self.output_value

    def bw_pass(self, loss_gradient):
        calc_gradient = loss_gradient * self._f_derivative(self.calc_value)
        self.gradient_ws = np.outer(calc_gradient, self.inputs)
        self.gradient_b = np.sum(calc_gradient, axis=0)
        self.gradient_inputs = np.dot(calc_gradient, self.ws)
        return self.gradient_inputs
