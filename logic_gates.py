from neural_network import NeuralNetwork
import numpy as np


class XOR:

    # XOR is created as follows:
    # A XOR B = (A NAND B) AND (A OR B)
    def __init__(self):
        self.neuralnetwork = NeuralNetwork([2, 2, 1])
        w_1 = self.neuralnetwork.getLayer(0)
        w_1.fill(0)
        # Layer 1 is a 2D array. The first row (here column) represents OR. The second represents NAND
        w_1 += np.array([[20, -20], [20, -20], [-10, 30]])
        w_2 = self.neuralnetwork.getLayer(1)
        w_2.fill(0)
        # Layer 2 represents an AND operation
        w_2 += np.array([[20], [20], [-30]])
        # print("__init__ has been called")

    def __call__(self, x, y):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        self.y = y * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = self.forward() == 1
        return z

    def forward(self):
        return self.neuralnetwork.forward([[self.x], [self.y]])


class AND:

    def __init__(self):
        self.neuralnetwork = NeuralNetwork([2, 1])
        w = self.neuralnetwork.getLayer(0)
        w.fill(0)
        w += np.array([[20], [20], [-30]])
        # print("__init__ has been called")

    def __call__(self, x, y):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        self.y = y * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = z[0]  # So that the output is a boolean and not a list containing a boolean
        return z[0]

    def forward(self):
        return self.neuralnetwork.forward([[self.x], [self.y]])


class OR:

    def __init__(self):
        self.neuralnetwork = NeuralNetwork([2, 1])
        w = self.neuralnetwork.getLayer(0)
        w.fill(0)
        w += np.array([[20], [20], [-10]])
        # print("__init__ has been called")

    def __call__(self, x, y):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        self.y = y * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = z[0]  # So that the output is a boolean and not a list containing a boolean
        return z[0]

    def forward(self):
        return self.neuralnetwork.forward([[self.x], [self.y]])


class NOT:

    def __init__(self):
        self.neuralnetwork = NeuralNetwork([1, 1])
        w = self.neuralnetwork.getLayer(0)
        w.fill(0)
        w += np.array([[-20], [10]])
        # print("__init__ has been called")

    def __call__(self, x):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = self.forward() == 1
        z = z[0]  # So that the output is a boolean and not a list containing a boolean
        return z[0]

    def forward(self):
        return self.neuralnetwork.forward([[self.x]])


if __name__ == "__main__":

    And = AND()  # Calls the __init__
    Or = OR()    # Calls the __init__
    Not = NOT()
    Xor = XOR()
    # print(And(False, True))  # __call__ is used. Now the object can be used as function
    # print(Xor(True, False))
