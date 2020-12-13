# Jessica Schonhut-Stasik 
# Homework 3

# JSS - Import modules 
import numpy as np 
import matplotlib.pyplot as plt 

def integration(x, y):
    
    width = max(x) / len(y)
    print('The width of each bin is: ' + str(width))
    z = width * y
    total_val = np.sum(z)

    return z, total_val

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

z, total_val = integration(x, y)
print(total_val)

plt.bar(x, y) 
plt.plot(x, z, color='red')
plt.title('Area of Integration = ' + str(total_val)) 
plt.savefig('integration_test.png')
plt.clf()


