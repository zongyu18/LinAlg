import numpy as np

f = open("GaltonFamilies.csv")
data = f.readlines()
f.close()

matrixAMale = []
matrixBMale = []
matrixAFemale = []
matrixBFemale = []

for i in range(1, len(data)):
    datapoint = data[i].split(',')
    if datapoint[7] == "male":
        matrixAMale.append(np.array([float(datapoint[2]),float(datapoint[3]), 1]))
        matrixBMale.append(np.array([float(datapoint[8])]))
    elif datapoint[7] == "female":
        matrixAFemale.append(np.array([float(datapoint[2]),float(datapoint[3]), 1]))
        matrixBFemale.append(np.array([float(datapoint[8])]))
"""
matrixAMale = []
matrixBMale = []
matrixAMale.append([67, 78.5, 1])
matrixBMale.append([69.2])
matrixAMale.append([67, 78.5, 1])
matrixBMale.append([69.0])
matrixAMale.append([66.5, 75.5, 1])
matrixBMale.append([65.5])
matrixAMale.append([64, 75, 1])
matrixBMale.append([68])
"""

males = (np.linalg.inv(np.transpose(matrixAMale) @ matrixAMale)) @ np.transpose(matrixAMale) @ matrixBMale
print(males)
females = (np.linalg.inv(np.transpose(matrixAFemale) @ matrixAFemale)) @ np.transpose(matrixAFemale) @ matrixBFemale
print(females)
