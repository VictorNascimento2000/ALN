import numpy as np
A = np.matrix([[0, 4, 1], [1, 1, 3], [2, -2, 1]])
b = np.array([9, 6, -1])

n = A.shape[0]
intch = np.zeros(n)
flag = 'A é singular'
print(A)

def Gauss(A, n, intch, flag):
    for k in range(0,n):
        amax = float('-inf')
        m = k
        for i in range(0,n-1):
            val = abs(A[i,k])
            if  val > amax:
                amax = val
                m = i
        if amax == 0:
            print(flag)
        else:
            intch[k] = m
            if m != k:
                A[(m, k), :] = A[(k, m), :]
            for i in range(k+1,n):
                A[i,k] = A[i,k]/A[k,k]
            for i in range(k+1,n):
                A[i,k:] = A[i,k]*


        
        
Gauss(A, n, intch, flag)
