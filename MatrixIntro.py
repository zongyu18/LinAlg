# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
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
    for i in range (len(M[row])):
      M[rowOne][i] += float(scalar) * M[rowTwo][i]
  except:
    print("Make sure that your scalar multiple is valid!"
