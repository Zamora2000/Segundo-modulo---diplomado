# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 22:30:07 2022

@author: Alvaro Zamora

# Alvaro José Zamora Cury
# identificación: 1003064557
# celular:3016842661
# correo: alvaro.zamora@upb.edu.co
# ID: 502225
# Taller #1, segundo módulo

"""

# Procedemos armar nuestra lista
        
N1 = [1]
N2 = [2]
N3 = [3]
N4 = [4]
N5 = [5] 
N6 = [6]

#Creamos nuestro vector el cual contendrá nuestras variables

Vector = [N1, N2, N3, N4, N5, N6]
           
           
# Primera ecuación
           
Ecuacion1 = (Vector[0][0]+(Vector[1][0]/Vector[2][0]))/(Vector[3][0]+(Vector[4][0]/Vector[5][0]))
           
# Segunda ecuación 

Ecuacion2 = Vector[0][0]-(Vector[1][0]/(Vector[2][0]-Vector[3][0]))
            
 
# Primero mostraremos nuestros valores originales

print ("Valores Originales")

print("\n Valor de la primera ecuación:")
print(Ecuacion1)
print("\n Valor de la segunda ecuación:")
print(Ecuacion2)
           
# Ahora mostramos los valores intercambiados
 
Ecu3 = Ecuacion2
Ecu4 = Ecuacion1
          
print("\n Valores intercambiados")

print("\n Valor de la primera ecuación luego del intercambio:")
print(Ecu3)
print("\n Valor de la segunda ecuación luego del intercambio:")
print(Ecu4)

