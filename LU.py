import numpy as np
A = np.matrix([[2, 10, 8, 8, 6], [1, 4, -2, 4, -1], [0, 2, 3, 2, 1], [3, 8, 3, 10, 9], [1, 4, 1, 2, 1]], dtype=float)

n = A.shape[0]
intch = np.zeros(n)
flag = 'A é singular'
print(A)

def Gauss(A, n, intch, flag):
    for k in range(0,n):
        amax = float('-inf')
        m = k
        for i in range(k,n):
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
                A[i,k+1:] = A[i,k+1:] - A[i,k]*A[k,k+1:] 
    if A[n-1, n-1] == 0:
        print(flag)
        intch[n-1] = 0
    else:
         intch[n-1] = n-1
    print(A)
    print(intch)

Gauss(A, n, intch, flag)
