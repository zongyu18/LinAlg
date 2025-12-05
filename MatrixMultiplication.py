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
    rowNum = rows(M)
    tempList = []
    for k in range(cols(M)):
      tempList.append(N[k][j])
    return dotProduct(vectorOne, tempList)
  except:
    print("Your request could not be processed. Please try again.")
    return False
    
print(matrixMultiplicationElement(M, N,0,0))
