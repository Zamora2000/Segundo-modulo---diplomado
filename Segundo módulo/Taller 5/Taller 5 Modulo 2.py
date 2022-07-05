# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 00:22:56 2022

@author: Alvaro Zamora

# Alvaro José Zamora Cury
# identificación: 1003064557
# celular:3016842661
# correo: alvaro.zamora@upb.edu.co
# ID: 502225
# Taller #5, segundo módulo

"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from sklearn.metrics import r2_score

## convertimos el archivo csv en un data frame 

dato = pd.read_csv('AirQualityUCI.csv',sep=';')

## selecionamos los datos X y Y para relalizar nuestra regresion 
#  obtenemos el 20% de los datos para hacer las pruebas 

x = dato["NO2(GT)"].head(200)
y = dato["NOx(GT)"].head(200)
    
print ("Regresión Lineal ")

# Graficamos x con respecto a Y 

def grafico1_RLineal():
    plt.scatter(x,y)
    plt.xlabel("NO2(GT)")
    plt.ylabel("NOx(GT)")
    plt.title("NO2 vs NOx")

grafico1_RLineal()

# Ahora calculamos nuestro valor en R

def R():
    
    slope,intercept,r,p,std_err = stats.linregress(x,y)
    
    return slope,intercept,r,p,std_err

# Seguimos haciendo nuestro cálculo de los varios de nuestra regresión linear, para así ir a graficar

def regresion(x):
    
    slope,intercept,r,p,std_err=R()
    
    return slope * x + intercept

# Ahora graficamos la linea de la regresión 
 
def grafico2_RLineal():
    
    reg_model = list(map(regresion,x))
    
    plt.plot(x,reg_model)
    
    plt.show()
    
grafico2_RLineal()

slope,intercept,r,p,std_err=R()


print("Valor de R: " + str(r))
print ("-------------------------------------------------------------\n")

print ("\n Regresion Polinomial ")


def Regresion_Polinomial():
    
    poli_model = np.poly1d(np.polyfit(x,y,6)) 
    
    poli_line = np.linspace(2,200,100)
    
    plt.scatter(x,y)
    
    plt.plot(poli_line,poli_model(poli_line))
    
    plt.show()
    
    print(r2_score(y,poli_model(x)))
    
Regresion_Polinomial()
