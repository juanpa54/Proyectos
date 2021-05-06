##################################################
##          Universidad Sergio Arboleda         ##
##  Escuela de Ciencias exactas e Ingeniería    ##
##  Ingeniería de Sistemas y Telecomunicaciones ##
##                                              ##
## Algoritmo que calcula la potencia de un      ##
## número por recursividad.                     ##
##                                              ##
## Autores:                                     ##
##    -Juan Pablo Blanco                        ##
##    juan.blanco01@correo.usa.edu.co           ##
##                                              ##
## Fecha: 05/05/21                              ##
##################################################
from functionE import rbf_network
import  cy_functionE 
import numpy as np
import time
import matplotlib.pyplot as plt

D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

inicio = time.time()
rbf_network(X, beta, theta)
tiempoPy = time.time() - inicio

inicio = time.time()
cy_functionE.rbf_network(X, beta, theta)
tiempoCy = time.time() - inicio

speedUp = round(tiempoPy/tiempoCy,3)

print(f'Tiempo python : {tiempoPy}\n')
print(f'Tiempo Cython: {tiempoCy}\n')
print("SpeedUp: {}\n".format(speedUp))

fig, ax = plt.subplots()
etiquetas = ["Tiempo python", "Tiempo Cython"]
tiempos = [tiempoPy, tiempoCy]

ax.set_ylabel("Tiempo")
plt.bar(etiquetas, tiempos, width=0.3, color=["green", "orange"], align='center')
plt.savefig('graficaTiempos.png')
plt.grid()
plt.show()