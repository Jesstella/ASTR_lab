# Jessica Schonhut-Stasik
# Homework 2 - Problem 1

# Import modules 
import time
import numpy as np 
import matplotlib.pyplot as plt

# Equation: x**3 - 5*x + 2

t0 = time.time()

def forward(a, h):
    '''
    Forward difference formula is f'(a) ~ f(a+h) - f(a) / h 
    '''

    x = a+h
    term_1 = x**3 - (5 * x) + 2
    term_2 = a**3 - (5 * a) + 2
    f = (term_1 - term_2) / h

    return f

def central(a, h): 
    '''
    Central difference formula is f'(a) ~ f(a+h) - f(a-h) / 2h 
    '''    

    x = a+h 
    y = a-h
    term_1 = x**3 - (5 * x) + 2
    term_2 = y**3 - (5 * y) + 2
    f = (term_1 - term_2) / (2 * h)

    return f

if __name__ == '__main__':

    a = np.arange(-5, 5, 0.01) 
    h = 0.01 

    forward_f = forward(a, h)
    central_f = central(a, h) 

    plt.plot(a, forward_f)
    plt.plot(a, central_f)
    plt.savefig('both_derivatives.png')
    plt.clf()

    diff = abs(forward_f - central_f)
    plt.plot(a, diff)
    plt.savefig('difference.png')
    plt.clf() 

    t1 = time.time()
    total = t1 - t0 
    print('This code takes ' + str(total/60) + ' seconds to run.')

 
