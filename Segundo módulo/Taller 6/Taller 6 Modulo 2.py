# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 00:25:57 2022

@author: Alvaro Zamora

# Alvaro José Zamora Cury
# identificación: 1003064557
# celular:3016842661
# correo: alvaro.zamora@upb.edu.co
# ID: 502225
# Taller #6, segundo módulo

"""

# Primero importamos nuestras librerías 
import pandas as pd
from sklearn import tree 
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt 
import matplotlib.image as pltimg
import pydotplus
import statsmodels.api as sm 
import numpy as np

#Creamos un DataFrame con los set de datos Carseats
 
carseats = sm.datasets.get_rdataset("Carseats","ISLR")

datos = carseats.data

# print(carseats.__doc__)

# Con la variable Sale se crea una nueva variable dicotómica, se dividen en ventas altas
# donde si son mayores a 8 se cambia el valor a 0, pero si son ventas bajas se cambia de 8 a 1

datos['Ventas_Altas']= np.where(datos.Sales > 8,0,1)

# Aquí procedemos a eliminar la columna Sale

datos= datos.drop(columns='Sales')

# Vamos a cambiar los datos no númericos por una etiqueta númerica para identicarlos y hacer las operaciones 

# Creamos nuestro diccionario con la columna shelveloc, para tomar esos datos

d = {'Good':0,'Medium':1,'Bad':2}

# Mapeamos nuestros datos del diccionario anterior

datos['ShelveLoc'] = datos['ShelveLoc'].map(d)

# Creamos otro diccionario, esta vez con los datos de la columna Urban

d = {'Yes':0,'No':1}

# Hacemos otro mapeo de nuestro diccionario

datos['Urban']= datos['Urban'].map(d)

# Creamos otro diccionario, ahora con los datos de la columna US

d ={'Yes':0,'No':1} 

# Mapeamos nuestros datos del diccionario US

datos['US']= datos['US'].map(d)

# Ahora creamos una lista con los datos independientes, o variables independientes

feature = ['CompPrice','Income','Advertising','Population','Price','ShelveLoc','Age','Education','Urban','US']
 
# Ahora creamos nuestra variable o eje X usando los valores anteriores de features

x = datos[feature]

# Seguimos ahora con nuestra varible o eje Y con nuestra columna de destino

y = datos['Ventas_Altas']

# Ahora seleccionamos el 80% de los datos, esto con el fin de definir los datos de entrenamiento

train_x= x[:320]

train_y= y[:320]

# Ahora seguimos seleccionando el 20% restante como datos prueba

test_x= x[320:]

test_y= y[320:]

# Seguimos con la creación del arbol de decisión

dtree = DecisionTreeClassifier()

# Ajustamos los datos a nuestro modelo usando los datos de entrenamiento

dtree = dtree.fit(train_x,train_y)

# Exportamos los datos, para así poderlos graficar en nuestro diagrama de flujo

data = tree.export_graphviz(dtree, out_file=None, feature_names = feature)

# A continuación se crea nuestra gráfica

graph = pydotplus.graph_from_dot_data(data)

# Guardamos nuestra gráfica del arbol de decisión en formato .png

graph.write_png('arbol_de_decision_ventas.png')

# Abrimos la gráfica, y continuamos a mostrarla por pantalla

img = pltimg.imread('arbol_de_decision_ventas.png')

imgplot = plt.imshow(img)

plt.show()

# Hacemos la predicción con los datos obtenidos con los datos de prueba

data_prediccion= np.array(test_x)
print("\n")
print ("CompPrice: "+str(data_prediccion[0][0]))
print ("Icome: "+str(data_prediccion[0][1]))
print ("Advertissing: "+str(data_prediccion[0][2]))
print ("Population: "+str(data_prediccion[0][3]))
print ("Price: "+str(data_prediccion[0][4]))
print ("ShelveLoc: "+str(data_prediccion[0][5]))
print ("Age: "+str(data_prediccion[0][6]))
print ("Education: "+str(data_prediccion[0][7]))
print ("Urban: "+str(data_prediccion[0][8]))
print ("US: "+str(data_prediccion[0][9])+"\n")

print ("Prediccion")
print (dtree.predict([[data_prediccion[0][0],data_prediccion[0][1],data_prediccion[0][2],data_prediccion[0][3],data_prediccion[0][4],data_prediccion[0][5],data_prediccion[0][6],data_prediccion[0][7],data_prediccion[0][8],data_prediccion[0][9]]]))

# Hacemos la impresión de la ayuda para las respuestas

print ("[1] mean 'Ventas Altas'")
print ("[0] mean 'Ventas Bajas'")