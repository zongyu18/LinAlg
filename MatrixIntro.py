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
                sumRow(M, rowPointer, j, M[j][colPointer] * (-1))
        rowPointer += 1
        colPointer += 1

def RREF(M):
    REF(M)
    rowPointer = len(M) - 1
    while rowPointer >= 0:
        pivotPointer = -1
        for i in range(len(M[0])):
            if M[rowPointer][i] != 0:
                pivotPointer = i
                break
        if pivotPointer != -1:
            for i in range(0, rowPointer):
                sumRow(M, rowPointer, i, M[i][pivotPointer] * -1)
        rowPointer -= 1

r_1 = [4, 2]
r_2 = [3, 2]
r_3 = [1, 5]
M = [r_1, r_2, r_3]
RREF(M)
print(tabulate(M))
