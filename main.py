from perceptronClass import Perceptron
from readData import ReadData
from drawPoints import DrawPoints

p = Perceptron()

inputs = [-1, 0.5]
print(p.guess(inputs))

readData = ReadData()
readData.read()

drawPoints = DrawPoints()
drawPoints.draw()

for x, y, z in zip(readData.x, readData.y, readData.z):
    inputs = [x,y]
    p.train(inputs, z)
