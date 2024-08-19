import numpy as np
###################################################################
#Examples
#A = np.matrix([[1, 4, 7, 5], [2, 5, 8, 10], [3, 6, 9, 1], [5, 7, 9, 3]], dtype=float)
#A = np.matrix([[1, 0, 1, 1], [1, 5, 0, 9], [0, 9, 9, 6], [5, 10, 1, 0]], dtype=float)
#A = np.matrix([[1, 1], [-1, 1], [1, 2],[3, 6], [7, 7]], dtype=float)
#A = np.matrix([[1, 0], [1, 5], [0, 9], [5, 10]], dtype=float)
#A = np.matrix([[0, 1], [5, 1], [9, 0], [10, 5]], dtype=np.float64)
A = np.matrix([[1, 1], [1, 2], [1, 3], [1, 4] ,[1, 5]],dtype=np.float64)
###################################################################

def cos_sin(a,b):
    hipot = np.sqrt(a**2 + b**2)
    cos = a/hipot
    sin = b/hipot
    return cos, sin, hipot

def qr_rotators(A):
    m, n = A.shape
    R = A.copy()
    Q = np.identity(m)
    for i in range(0, n):
        for j in range(i+1, m):
            Q_temp = np.identity(m)
            cos, sin, h = cos_sin(R[i,i], R[j,i])
            Q_temp[i,i] = cos
            Q_temp[i,j] = sin
            Q_temp[j,i] = -sin
            Q_temp[j,j] = cos
            R = Q_temp @ R
            Q = Q_temp @ Q

    return Q, R

Q, R = qr_rotators(A)
print(Q.T)
print(np.round(R, 5))
print(np.round(Q.T @ R, 9))
###################################################################

# Correct answer
q, r =  np.linalg.qr(A) 
  
# Print the result 
print("Correct decomposition of matrix:") 
print( "q=\n", q, "\nr=\n", r)
