import numpy as np
import math

def detHelper(A):
    try:
        if len(A) == 1:
            return A[0][0]
        elif len(A) == 2:
            return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    except:
        print("Make sure that your matrix is a valid square matrix.")

A = np.array([[2, 3], [4, 9]])
print(detHelper(A))
