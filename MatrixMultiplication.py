def rows(M):
  return len(M)

def cols(M):
  try:
    return len(M[0])
  except:
    return -1
