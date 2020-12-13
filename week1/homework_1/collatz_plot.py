# Jessica Schonhut-Stasik 
# Assignment 1 - Plotting Collatz Lists

# Import Modules 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

collatz = pd.read_csv('collatz_list_code_output.txt', delimiter=',')
n = collatz['# N']
l = collatz[' l(N)']

print('The length of this file is: ' + str(len(n)))

range_1 = np.linspace(1, 100, 100, dtype=int) 
range_2 = np.linspace(1, 1000, 1000, dtype=int) 
range_3 = np.linspace(1, 10000, 10000, dtype=int)

l_one = l[0: 100]
l_two = l[0: 1000]
l_three = l[0: 10000]

a = 1
def plot(n_list, l_list):
    plt.figure()
    plt.scatter(n_list, l_list)
    plt.savefig('plot_range_' + str(a) + '.png')
    plt.clf()

plot(range_1, l_one)
a = 2
plot(range_2, l_two)
a = 3
plot(range_3, l_three) 
