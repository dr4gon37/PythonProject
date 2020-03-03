from random import seed
from random import gauss
seed(1)

class Perceptron:
    theSizeOfWeights = 2
    def __init__(self):
        self.__weights = []
        self.lr = 0.1
        i = 0
        while i < self.theSizeOfWeights:
            self.__weights.append(gauss(-1,1))
            i+=1

    def sign(self,n):
        if (n>=0):
            return 1
        else:
            return -1

    def guess(self, inputs):
        sum = 0
        for i, j in zip(inputs, self.__weights):
            sum += i * j
        output = self.sign(sum)
        return output

    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        index = 0
        for i, j in zip(inputs, self.__weights):
            j += error * i * self.lr
            self.__weights[index] = j
            index+=1
