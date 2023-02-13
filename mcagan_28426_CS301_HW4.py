# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 17:36:50 2022

@author: melih
"""

#MELİH ÇAĞAN ARI 28426

from matplotlib import pyplot as plt
import time
shortest_path = []
def func(n,m,V, A, sp ):
    strn = str(n)
    strm = str(m)
   
    
    mevcut = strn + "," + strm +" "
    if A[n][m] != -1:
        return A[n][m]
    elif n == 0 and m == 0:
        A[n][m] = V[n][m]
        sp[n][m] = mevcut
        
        return A[n][m]
    elif n == 0:
        A[n][m] = V[n][m] + func(n, m-1, V, A, sp)
        sp[n][m] = mevcut + sp[n][m-1]
        return A[n][m]
    elif m == 0  :
        
        A[n][m] = V[n][m] + func(n-1, m, V, A, sp)
        sp[n][m] = mevcut + sp[n-1][m]
        
        return A[n][m]
    else :
        A[n][m] = V[n][m] + max( func(n, m-1, V, A, sp),func(n-1, m, V, A, sp) )

        if func(n, m-1, V, A, sp) >= func(n-1, m, V, A, sp):
            sp[n][m] = mevcut + sp[n][m-1]
        else:
            sp[n][m] = mevcut +  sp[n-1][m]
        #print(A[n][m]  , "yeyeyeyeye", n, m, A[n-1][m], A[n][m-1])
        return A[n][m]
 
runningTimes = []
coordinates = []    
 
rows, cols = 5, 6
V = [[1,0,1,0,0,0],[0,1,0,1,0,0 ],[0,1,1,0,0,0],[0,0,0,0,1,0],[1,0,1,0,0,1]]
A = [[-1 for i in range(cols)] for j in range(rows)]
shortest_path = [["" for i in range(cols)] for j in range(rows)]
val1 = time.time() 
print(func(rows-1,cols-1, V, A, shortest_path))
print("SHORTEST PATH")
print(shortest_path[rows-1][cols-1])

val2 = time.time()

elapsed_time = val2 - val1
runningTimes.append(elapsed_time)
xy = "("+str(rows) + ", " + str(cols)+")" 
coordinates.append(xy)


    
rows, cols = 12, 6
V = [[1,0,1,0,0,0],[0,1,0,1,0,0 ],[0,1,1,0,1,0],[0,0,0,0,1,0],[1,0,1,0,0,1],
     [1,0,1,0,0,0],[1,0,1,0,1,0],[0,0,1,1,0,0],[0,0,1,0,1,0],[0,0,1,0,0,0],
     [0,0,1,0,1,1],[1,0,1,0,1,0]]
A = [[-1 for i in range(cols)] for j in range(rows)]
shortest_path = [["" for i in range(cols)] for j in range(rows)]
val1 = time.time()
print(func(rows-1,cols-1, V, A,shortest_path))
print("SHORTEST PATH")
print(shortest_path[rows-1][cols-1])
val2 = time.time()

elapsed_time = val2 - val1
runningTimes.append(elapsed_time)
xy = "("+str(rows) + ", " + str(cols)+")" 
coordinates.append(xy)





    
rows, cols = 5, 10
V = [[1,0,1,0,0,0,1,1,0,0],[0,1,0,1,0,0,0,1,0,1 ],[0,1,1,0,0,0,0,0,1,1],[0,0,0,0,1,0,0,1,1,1],[1,0,1,0,0,1,1,0,0,0]]
A = [[-1 for i in range(cols)] for j in range(rows)]
shortest_path = [["" for i in range(cols)] for j in range(rows)]
val1 = time.time()
print(func(rows-1,cols-1, V, A , shortest_path))
print("SHORTEST PATH")
print(shortest_path[rows-1][cols-1])
val2 = time.time()

elapsed_time = val2 - val1
runningTimes.append(elapsed_time)
xy = "("+str(rows) + ", " + str(cols)+")" 
coordinates.append(xy)




    
rows, cols = 10, 10
V = [[1,0,1,0,0,0,1,1,0,1],[1,0,1,0,1,0,1,1,0,1],[1,0,1,0,0,0,1,0,0,1],
     [0,0,1,0,0,0,1,1,0,1],[0,0,1,0,0,1,1,1,0,1],[1,0,1,0,0,0,0,0,1,1],
     [1,0,1,0,0,0,1,1,0,1],[0,0,1,0,0,0,1,0,0,1],[0,0,1,0,1,0,1,0,0,1],
     [0,1,1,0,0,0,1,0,0,1]]
A = [[-1 for i in range(cols)] for j in range(rows)]
shortest_path = [["" for i in range(cols)] for j in range(rows)]

val1 = time.time()
print(func(rows-1,cols-1, V, A,shortest_path))
print("SHORTEST PATH")
print(shortest_path[rows-1][cols-1])
val2 = time.time()

elapsed_time = val2 - val1
runningTimes.append(elapsed_time)
xy = "("+str(rows) + ", " + str(cols)+")" 
coordinates.append(xy)



    
rows, cols = 15, 10
V = [[1,0,1,0,0,0,1,0,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,0,1,0,1,1,0,1],
     [1,1,1,0,0,0,1,0,0,1],[1,0,1,0,0,0,1,0,0,0],[0,0,1,0,1,1,1,1,1,1], 
     [0,1,1,0,1,0,0,1,0,0],[0,0,1,1,0,0,0,1,0,1],[0,0,1,0,0,0,1,1,0,0],
     [0,0,1,0,0,0,1,1,0,0],[1,0,1,0,0,1,1,1,0,0],[1,1,1,0,0,0,1,1,0,1],
     [0,1,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,1,1,0,1],[1,0,1,0,1,0,1,1,0,1]]
A = [[-1 for i in range(cols)] for j in range(rows)]
shortest_path = [["" for i in range(cols)] for j in range(rows)]

val1 = time.time()
print(func(rows-1,cols-1, V, A , shortest_path))
print("SHORTEST PATH")
print(shortest_path[rows-1][cols-1])
val2 = time.time()

elapsed_time = val2 - val1
print(elapsed_time)
runningTimes.append(elapsed_time)
xy = "("+str(rows) + ", " + str(cols)+")" 
coordinates.append(xy)


plt.plot( coordinates,runningTimes)
plt.show()
