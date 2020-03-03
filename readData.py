class ReadData:
    def __init__(self):
        ReadData.x = []
        ReadData.y = []
        ReadData.z = []
    def read(self):
        for l in open("DataTraining.txt", "r"):
            row = l.split()
            ReadData.x.append(float(row[0]))
            ReadData.y.append(float(row[1]))
            ReadData.z.append(float(row[2]))

