import numpy as np
import math


class NeuralNetwork:

    def __init__(self, layer_sizes=[]):
        self.layer_sizes = layer_sizes
        self.theta = []
        for i in range(0, len(self.layer_sizes) - 1):
            random_normal_vector = np.random.normal(0, 1 / math.sqrt(self.layer_sizes[i] * self.layer_sizes[i + 1]), (1 + self.layer_sizes[i]) * self.layer_sizes[i + 1])
            random_normal_matrix = np.reshape(random_normal_vector, (1 + self.layer_sizes[i], self.layer_sizes[i + 1]))
            self.theta.append(random_normal_matrix)

    def getLayer(self, layer):
        return self.theta[layer]

    def forward(self, input):
        # ======================(Important)======================
        # input is assumed to be a column vector, or a batch of column vectors
        # forward() will work with 1D (single vectors) or 2D inputs (batches)
        # Everytime a (theta)transpose * x is computed, a bias of 1 is added to the x (input)

        y = input
        # If dim = 2, then you will add the bias for each vector in the batch
        # e.g., input = [[0,0,0],[0,0,0]]
        # input after adding bias = [[0,0,0], [0,0,0], [1,1,1]]
        if np.ndim(y) == 2:
            for i in range(0, len(self.layer_sizes) - 1):
                input_r, input_c = np.shape(y)
                bias = np.ones([1, input_c])
                y = np.append(y, bias, axis=0)
                y = np.matmul(self.theta[i].transpose(), y)
                y = np.round(1 / (1 + np.exp(-y)))

        # if dim = 1, then just add bias at the end
        if np.ndim(y) == 1:
            bias = 1
            for i in range(0, len(self.layer_sizes) - 1):
                # Calculates Theta(transpose) times X
                y = np.append(y, bias)
                y.reshape(len(y), 1)
                y = np.matmul(self.theta[i].transpose(), y)
                y = np.round(1 / (1 + np.exp(-y)))

        return y


# if __name__ == "__main__":
#     model = NeuralNetwork([2, 2, 1])
#     x = np.array([[1], [1]])
#     y = model.forward(x)
#     w = model.getLayer(0)
#     print(w)
