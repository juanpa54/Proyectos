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
from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

exts=(cythonize('cy_functionE.pyx'))
setup(ext_modules=exts, 
      include_dirs=[numpy.get_include()])
