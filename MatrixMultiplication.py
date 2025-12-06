import copy
import tabulate

M = [[1,2], [0,-1],[3,4]]
N = [[2, 5], [3, 4]]
def rows(M):
  return len(M)

def cols(M):
  try:
    return len(M[0])
  except:
    return -1

def validMultiplication(M, N):
  try:
    if cols(M) == rows(N):
      return True
    else:
      return False
  except:
    return False

def dotProduct(M, N):
  sum = 0
  try:
    for i in range(len(M)):
      sum += M[i] * N[i]
    return sum
  except:
    print("The inputted vectors could not be dotted.")
    return False

def matrixMultiplicationElement(M, N, i, j):
  try:
    vectorOne = M[i]
    tempList = []
    for k in range(cols(M)):
      tempList.append(N[k][j])
    return dotProduct(vectorOne, tempList)
  except:
    print("Your request could not be processed. Please try again.")
    return False

def matrixMultiplication(M, N):
  tempList = []
  for k in range(rows(M)):
    tempList.append([])
    for l in range(cols(N)):
      tempList[k].append(matrixMultiplicationElement(M, N, k, l))
  return tempList

def transpose(M):
    tempList = []
    row = rows(M)
    col = cols(M)
    for i in range(col):
        tempList.append([])
        for j in range(row):
            tempList[i].append(M[j][i])
    return tempList

def convertZ2(M):
    for i in range(rows(M)):
        for j in range(cols(M)):
            M[i][j] %= 2
    return M

def multiplyZ2(M, N):
    return matrixMultiplication(convertZ2(M), convertZ2(N))

print("The results of multiplying M by N")
print("-----------------------------------")
print(tabulate.tabulate(matrixMultiplication(M, N)))
print("Original Matrix")
print("-----------------------------------")
print(tabulate.tabulate(M))
print("Transposed Matrix")
print("-----------------------------------")
print(tabulate.tabulate(transpose(M)))
print("Original Matrix")
print("-----------------------------------")
print(tabulate.tabulate(M))
print("Converted Matrix")
print("-----------------------------------")
print(tabulate.tabulate(convertZ2(M)))
print("Converted Matrix Multiplication")
print("-----------------------------------")
print(tabulate.tabulate(multiplyZ2(M, N)))
