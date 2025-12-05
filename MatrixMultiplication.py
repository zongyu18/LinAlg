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
    for i in range(len(M))):
      sum += M[i] * N[i]
    return sum
  except:
    print("The inputted vectors could not be dotted.")
    return False

def matrixMultiplicationElement(M, N, i, j):
  try:
    vectorOne = M[i]
    rowNum = rows(M)
    tempList = []
    for k in range(rowNum):
      tempList.append(N[k][j])
    return dotProduct(vectorOne, tempList)
  except:
    print("Your request could not be processed. Please try again.")
    return False
