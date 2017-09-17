from neural_network import NeuralNetwork
import numpy as np
from random import randint


class XOR:

    # XOR is created as follows:
    # A XOR B = (A NAND B) AND (A OR B)
    def __init__(self):
        self.neuralnetwork = NeuralNetwork([2, 2, 1])
        for epoch in range(0, 1000):
            x1 = randint(0,1)
            x2 = randint(0,1)
            y = self.neuralnetwork.forward(np.array([[x1], [x2]]))
            target = x1 != x2
            # print("epoch number", epoch, "predicted value", y, "loss", y - target)
            self.neuralnetwork.backward(target)
            self.neuralnetwork.updateParams(0.4)
    
    def __call__(self, x, y):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        self.y = y * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = self.forward() == 1
         # So that the output is a boolean and not a list containing a boolean
        return z

    def forward(self):
        return self.neuralnetwork.forward(np.array([[self.x], [self.y]]))


class AND:

    def __init__(self):
        self.neuralnetwork = NeuralNetwork([2, 2, 1])
        for epoch in range(0, 1000):
            x1 = randint(0,1)
            x2 = randint(0,1)
            y = self.neuralnetwork.forward(np.array([[x1], [x2]]))
            target = x1 and x2
            # print("epoch number", epoch, "predicted value", y, "loss", y - target)
            self.neuralnetwork.backward(target)
            self.neuralnetwork.updateParams(0.4)

    def __call__(self, x, y):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        self.y = y * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = self.forward() == 1
          # So that the output is a boolean and not a list containing a boolean
        
        return z

    def forward(self):
        return self.neuralnetwork.forward(np.array([[self.x], [self.y]]))


class OR:

    def __init__(self):
        self.neuralnetwork = NeuralNetwork([2, 1])
        for epoch in range(0, 1000):
            x1 = randint(0,1)
            x2 = randint(0,1)
            y = self.neuralnetwork.forward(np.array([[x1], [x2]]))
            target = x1 or x2
            # print("epoch number", epoch, "predicted value", y, "loss", y - target)
            self.neuralnetwork.backward(target)
            self.neuralnetwork.updateParams(0.4)

    def __call__(self, x, y):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        self.y = y * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = self.forward() == 1

        return z

    def forward(self):
        return self.neuralnetwork.forward(np.array([[self.x], [self.y]]))


class NOT:

    def __init__(self):
        self.neuralnetwork = NeuralNetwork([1, 1])
        for epoch in range(0, 1000):
            x1 = randint(0,1)
            y = self.neuralnetwork.forward(np.array([[x1]]))
            target = 1- x1
            # print("epoch number", epoch, "predicted value", y, "loss", y - target)
            self.neuralnetwork.backward(target)
            self.neuralnetwork.updateParams(0.4)

    def __call__(self, x):
        # Converting Boolean into integer
        self.x = x * 1  # magically converts boolean to integer
        # print("__call__ has been called")
        z = self.forward() == 1
        return z

    def forward(self):
        return self.neuralnetwork.forward(np.array([[self.x]]))


if __name__ == "__main__":

    And = AND()  # Calls the __init__
    Or = OR()    # Calls the __init__
    Not = NOT()
    Xor = XOR()
    # print(And(False, True))  # __call__ is used. Now the object can be used as function
    print(Not(True))
