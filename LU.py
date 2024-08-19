import numpy as np
#A = np.matrix([[2, 10, 8, 8, 6], [1, 4, -2, 4, -1], [0, 2, 3, 2, 1], [3, 8, 3, 10, 9], [1, 4, 1, 2, 1]], dtype=float)
A = np.matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]], dtype=float) #Matriz singular
#A = np.matrix([[1000, 999],  [999,  998]], dtype=float)

####################################
import scipy.linalg as la
(P, L, U) = la.lu(A)
print('resposta correta:')
print(L)
print(U)
print('####################################')
####################################

n = A.shape[0]
intch = np.zeros(n)
global flag 
flag = False

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
            flag = True
        else:
            intch[k] = m
            if m != k:
                A[(m, k), :] = A[(k, m), :]
            
            for i in range(k+1,n):
                A[i,k] = A[i,k]/A[k,k]

            for i in range(k+1,n):
                A[i,k+1:] = A[i,k+1:] - A[i,k]*A[k,k+1:] 
                
    if A[n-1, n-1] == 0:
        flag = True
        intch[n-1] = 0
    else:
         intch[n-1] = n-1

    return A, intch, flag

A, intch, flag = Gauss(A, n, intch, flag)
print(A)
if flag == True:
    print('A é singular')
