# Jessica Schonhut-Stasik
# Assignment 1 - Outputs text file

import numpy as np
import time 

t0 = time.time()

x = np.linspace(1, 1000000000, 1000000000, dtype=int)

def odd(N):
    output = (3*N)+1
    return output

def even(N):
    output = N/2
    return output 

len_collatz_list = []
for i in x:
    collatz_list = []
    while i > 1:
        if i % 2 == 0: # even number 
            i = even(i)
            collatz_list.append(i) 
        else:
            i = odd(i)
            collatz_list.append(i)
    collatz_list.append(1)
    len_collatz_list.append(len(collatz_list) - 1)

t1 = time.time()
total = t1 - t0 
print('This code takes ' + str(total) + ' seconds to run.')

len_collatz_list = np.array(len_collatz_list) 

array = np.column_stack((x, len_collatz_list)) 

np.savetxt('collatz_list_code_output.txt', array, fmt='%i', delimiter=',',  header='N,l(N)')
