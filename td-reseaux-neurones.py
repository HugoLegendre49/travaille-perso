import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 1 +(np.sin(4*np.cos(x)))**2

def f_noisy(x):
    return f(x)+np.random.normal(0,0.1)

def generate_noisy_data(M):
    x_random = np.random.random(M)
    y_noisy = f_noisy(x_random)
    return x_random, y_noisy

def J_f (x,y,M):
    somme = 0
    for i in range(M):
        somme =+ (f(x[i])-y[i])**2
    return somme

def sigmoide(x):
    return 1/(1+np.exp(-x))

def sigmoide_prime(x):
    return (np.exp(-x))/(1+np.exp(-x))**2


x_r , y_r = generate_noisy_data(500)
y_sigma = sigmoide(x_r)

plt.scatter(x_r, y_r)
plt.show()
print("erreur quadratique de la fonction f est de : ",J_f(x_r,y_r,500))
plt.scatter (x_r,y_sigma)
plt.show()
