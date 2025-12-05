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
