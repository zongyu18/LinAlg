# Matrices as Lists of Lists
# Using Python for elementary row operations, REF, and RREF
# Andy Li

import copy
from tabulate import tabulate

def returnRow(M, row):
  return M[row]

def returnCol(M, col):
  return M[col]

def scalarRow(M, row, scalar):
  try:
    if scalar != 0:
      for i in range(len(M[row])):
        M[row][i] *= float(scalar)
  except:
    print("Make sure that your scalar multiple is valid!")

def sumRow(M, rowOne, rowTwo, scalar):
  try:
    for i in range (len(M[rowTwo])):
      M[rowTwo][i] += float(scalar) * M[rowOne][i]
  except:
    print("Make sure that your scalar multiple is valid!")

def interchange(M, rowOne, rowTwo):
  M[rowOne], M[rowTwo] = M[rowTwo], M[rowOne]
r_1 = [3, 4, 5]
r_2 = [5, 12, 13]
r_3 = [7, 24, 25]
M = [r_1, r_2, r_3]
sumRow(M, 1, 2, 3)
print(M)
