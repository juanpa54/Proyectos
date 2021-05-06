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
from math import exp
import numpy as np

def rbf_network(X, beta, theta):

    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y

