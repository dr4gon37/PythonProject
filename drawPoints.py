
from matplotlib import pyplot as plt
from readData import ReadData

class DrawPoints(ReadData):
    def __init__(self):
        self.x = ReadData.x
        self.y = ReadData.y
        self.z = ReadData.z
    def draw(self):
        #b = Bubblesort(self.x, self.y, self.z)
        #b.bubblesortX()
        #b.sort()
        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        for i in range (100):
            if self.z[i] == 1:
                ax1.scatter(self.x[i], self.y[i], s = 7, color = 'b', marker = 's')
            else:
                ax1.scatter(self.x[i], self.y[i], s = 7, color = 'r', marker = 'o')
        plt.xlabel("weight")
        plt.ylabel("height")
        plt.title("excersise 1")
        #plt.legend('red - man, blue - woman', loc = 'upper left')
        plt.show()
