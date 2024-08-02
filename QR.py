import numpy as np

A = np.matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]], dtype=float)

def cos_sin(a,b):
    hipot = np.sqrt(a**2 + b**2)
    cos = a/hipot
    sin = b/hipot
    return cos, sin, hipot

def qr_rotators(A):
    m, n = A.shape
    R = A.copy()
    Q = np.identity(m)
    for i in range(0, n-1):
        for j in range(i+1, m):
            Q_temp = np.identity(m)
            cos, sin, h = cos_sin(R[i,i], R[j,i])
            Q_temp[i,i] = cos
            Q_temp[i,j] = sin
            Q_temp[j,i] = -sin
            Q_temp[j,j] = cos
            #print(Q_temp)
            #print(R)
            R = Q_temp @ R
            #print(R)
            Q = Q_temp @ Q 

    return Q, R

Q, R = qr_rotators(A)
print(Q.T)
print(R)
print(Q.T @ R)
