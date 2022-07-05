# -*- coding: utf-8 -*-
"""
Created on Tue Jun  28 00:47:11 2022

@author: Alvaro Zamora

# Alvaro José Zamora Cury
# identificación: 1003064557
# celular:3016842661
# correo: alvaro.zamora@upb.edu.co
# ID: 502225
# Taller #7, segundo módulo

"""

#Librerias incluidas

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

print("#---------------------------Actividad con BD Cars Regresion Polinomial-------------------------------------")

# Importe de la base de datos

cars_df = pd.read_csv('cars2.csv')

# Variables independiente

x_cars = cars_df["Weight"]

#Definimos la variable dependiente

y_cars = cars_df["CO2"]

# Estandarización de las variables

scale_cars = StandardScaler()

scale_x_cars =(cars_df["Weight"]-cars_df["Weight"].mean())/cars_df["Weight"].std()

#Train / Test

x_train_cars = scale_x_cars[:28]
y_train_cars = y_cars[:28]

x_test_cars = scale_x_cars[28:]
y_test_cars = y_cars[28:]


# Gráfica de variables

plt.scatter(x_train_cars,y_train_cars)
plt.show()

plt.scatter(x_test_cars,y_test_cars)
plt.show()

# Modelo de Regresion Polinomial

poli_cars =  np.poly1d(np.polyfit(x_train_cars,y_train_cars,8))
myline = np.linspace(-3,2,90)

poli_new_y = poli_cars(myline)

# Gráfica del modelo

plt.scatter(x_train_cars,y_train_cars)
plt.plot(myline,poli_new_y )

plt.show()


#Predicción del modelo

print(poli_cars(0.4))

#R de relacion train y test

r2_train = r2_score(y_train_cars, poli_cars(x_train_cars))


poli_cars =  np.poly1d(np.polyfit(x_test_cars,y_test_cars,8))
myline = np.linspace(-3,2,90)

poli_new_y = poli_cars(myline)

#Gráfica del modelo

plt.scatter(x_train_cars,y_train_cars)
plt.plot(myline,poli_new_y)

plt.show()

r2_test = r2_score(y_test_cars, poli_cars(x_test_cars))

print(r2_train)
print(r2_test)



print("#---------------------------Actividad con BD Cars Regresion Multiple-------------------------------------")

# Importe de la base de datos

cars_df = pd.read_csv('cars2.csv')

# Variables independiente

x_cars = cars_df[["Weight","Volume"]]

#Definimos la variable dependiente

y_cars = cars_df["CO2"]

# Estandarizacion de las variables

scale_cars = StandardScaler()
scale_x_cars =scale_cars.fit_transform(x_cars)

#Train / Test

x_train_cars = scale_x_cars[:28]
y_train_cars = y_cars[:28]

x_test_cars = scale_x_cars[28:]
y_test_cars = y_cars[28:]


#Modelo de Regresion Multiple

modelo_cars = linear_model.LinearRegression()
modelo_cars.fit(x_train_cars,y_train_cars)

#Prediccion del modelo

pred_scale_x_cars = modelo_cars.predict([x_test_cars[0]])

print(pred_scale_x_cars)

#R de relacion train y test

print ("Valor de r de relacion de train ")
r2_train = r2_score(y_train_cars, modelo_cars.predict(x_train_cars))

print(r2_train)

#Modelo de Regresion Multiple

modelo_cars.fit(x_test_cars,y_test_cars)
print ("Valor de r de relacion de test ")
r2_test = r2_score(y_test_cars, modelo_cars.predict(x_test_cars))

print(r2_test)

#%%
# importamos las libreria 

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

#selecicionamos el archivo csv para convertirlo en un data frame
 
netflix =  pd.read_csv('netflix_titles.csv')

#convermitos os datos de tiempo a numericos 

netflix["duracion"] = pd.to_numeric(netflix['duration'].replace('([^0-9]*)','', regex=True), errors='coerce')

# Variables independiente

x_netflix = netflix["release_year"][:1000]       
            
#Definimos la variable dependiente

y_netflix = netflix["duracion"][:1000]

# Estandarizacion de las variables

scale_x_netflix =(x_netflix-x_netflix.mean())/x_netflix.std()

#Train / Test 
# datos de entrenamientos 

train_x_netflix = scale_x_netflix[:800]
train_y_netflix = y_netflix[:800]


# datos de prueba 

test_x_netflix = scale_x_netflix[800:]
test_y_netflix = y_netflix[800:]



#mostrar nuetro conjunto de entrenamiento

plt.scatter(train_x_netflix,train_y_netflix)
plt.show()

#mostrar nuetro conjunto de prueba

plt.scatter(test_x_netflix,test_y_netflix)
plt.show()

#Modelo de Regresion Polinomial

poli_netflix =  np.poly1d(np.polyfit(train_x_netflix,train_y_netflix,9))
myline = np.linspace(-6,1,300)
poli_new_y = poli_netflix(myline)

#GRafica del modelo

plt.scatter(train_x_netflix,train_y_netflix)
plt.plot(myline,poli_new_y )
plt.show()


#Prediccion del modelo

print(poli_netflix(-1))

#R de relacion train y test

print ("Valor de r de relacion de train ")
r2_train = r2_score(train_y_netflix, poli_netflix(train_x_netflix))
print(r2_train)

print ("Valor de r de relacion de test ")
r2_test = r2_score(test_y_netflix, poli_netflix(test_x_netflix))
print(r2_test)

## utilizando la variable de duracion y release_yea procesada por el medio de la regresion polinomial existe una relacion muy baja 
## esto quiere decir que el modelo no es el indicado para este problema

#%%

#importamos las librerias 

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


## convertimos el archivo csv en un data frame 

df= pd.read_csv('student_data.csv')

# creamos x y definimos las variables independiente 

x = df[['age','famrel']]

# cramos y y definimos la variables dependiente 

y = df[['traveltime']]


#mostrar nuetro conjunto de entrenamiento en diagrama de disperción 

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')
ax1.scatter(x["age"], x["famrel"],y, c='g', marker='o')

plt.show()


# estandarizamos los dato seleccionados 

scale = StandardScaler()
scaledx = scale.fit_transform(x)


# dividimos los datos 
#entrenamiento

train_x= scaledx[:315]
train_y= y[:315]

#prueba 

test_x= scaledx[315:]
test_y= y[315:]


## creamos nuetro modelo de regresion multiple

regre_mult= linear_model.LinearRegression()
regre_mult.fit(train_x,train_y)


#Prediccion del modelo 

print ("----- predicción ----")
pred_traveltime = regre_mult.predict([test_x[0]])

print(pred_traveltime)



print ("valor de r para conjuntos de datos de entrenamiento ")

# R de relacion train y test para nuestro modelo 

r2_train = r2_score(train_y, regre_mult.predict(train_x))

print(r2_train)


regre_mult.fit( test_x,test_y)


print ("valor de r para conjuntos de datos de prueba ")

r2_test = r2_score(test_y, regre_mult.predict(test_x))

print(r2_test)


## se pude observar que el R2 arrojo balores muy bajos lo que significa que nuetro modelo no es el apropiado para este problema 
