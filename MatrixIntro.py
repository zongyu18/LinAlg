# Matrices as Lists of Lists
# Using Python for elementary row operations, REF, and RREF
# Andy Li

import copy
from tabulate import tabulate

def returnRow(M, row):
  return M[row]

# Multiply all elements of a row by a scalar
def scalarRow(M, row, scalar):
  try:
    if scalar != 0:
      for i in range(len(M[row])):
        M[row][i] *= float(scalar)
    else:
        print("Your scalar has to be nonzero!")
  except:
    print("Make sure that your input is valid!")

# Add a scalar multiple of one row (rowOne) to another row (rowTwo)
def sumRow(M, rowOne, rowTwo, scalar):
  try:
    for i in range (len(M[rowTwo])):
      M[rowTwo][i] += float(scalar) * M[rowOne][i]
  except:
    print("Make sure that your input is valid!" + str(rowTwo))

# Interchange two rows of the matrix
def interchange(M, rowOne, rowTwo):
  M[rowOne], M[rowTwo] = M[rowTwo], M[rowOne]

def checkREF(M):
    colPointer = -1
    allZero = False
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 1:
                if j > colPointer and allZero == False:
                    colPointer = j
                    break
                else:
                    return False
            elif M[i][j] != 0:
                return False
            elif j == len(M[i]) - 1:
                allZero = True
    return True

def REF(M):
    rowPointer = 0
    colPointer = 0
    tempRowPointer = -1
    while rowPointer < len(M) and colPointer < len(M[rowPointer]):
        for i in range(rowPointer, len(M)):
            if M[i][colPointer] != 0:
                tempRowPointer = i
                break
        if tempRowPointer != -1:
            if tempRowPointer != rowPointer:
                interchange(M, tempRowPointer, rowPointer)
            tempRowPointer = -1
            scalarRow(M, rowPointer, M[rowPointer][colPointer] ** (-1))
            for j in range(rowPointer + 1, len(M)):
                sumRow(M, rowPointer, j, M[i][colPointer] * (-1))
        rowPointer += 1
        colPointer += 1
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = round(M[i][j], 1)
    while (not checkREF(M)):
        for i in range(len(M)):
            allZero = False
            for j in range(len(M[0])):
                if M[i][j] != 0:
                    break
                else:
                    if j == len(M[0]) - 1 and i < len(M) - 1:
                        interchange(M, i, i+1)
r_1 = [0, 0, 0]
r_2 = [3, 6, 0]
r_3 = [0, 0, 0]
M = [r_1, r_2, r_3]
REF(M)
print(tabulate(M))
