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
all:
		python3 setup.py build_ext --inplace
clean:
		rm -rf build *.so *.pyc *.c