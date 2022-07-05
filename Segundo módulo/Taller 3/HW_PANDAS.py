# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:36:10 2022

@author: Alvaro Zamora

# Alvaro José Zamora Cury
# identificación: 1003064557
# celular:3016842661
# correo: alvaro.zamora@upb.edu.co
# ID: 502225
# Taller #1, segundo módulo
"""

import pandas as pd
import numpy as np 

#Iniciamos leyendo nuestro contenido de la tabla, luego de importar nuestra librería

my_data = pd.read_excel(r'C:\Users\USUARIO\.spyder-py3\TablaEstudiantes.xlsx', sheet_name='InformacionE')



print("\n----------------------------- EJERCICIO 1 ----------------------------\n")

# EJERCICIO 1

## A partir de la tabla, usando el peso (en kg) y estatura (en metros),
## calcule el índice de masa corporal de cada individuo y lo almacene en
## una variable, Muestre por pantalla la frase “Tu índice de masa corporal
## es <imc>” donde <imc> es el índice de masa corporal calculado
## redondeado con dos decimales. 

#Armamos la fórmula

my_data["IMC"] = round(my_data['Peso (kg)']/(my_data['Altura']**2))

#Declaramos las variables a usar, y pasamos los datos por parámetro

var_imc = len(my_data['IMC'])
var_nombre = len(my_data['Nombre'])

#Hacemos un contador para almacenar la cuenta de los datos a mostrar

cont = 0

#Hacemos nuestro ciclo para mostrar el  IMC y concatenamos el nombre del estudiante

while cont < var_imc:
    
    print("Su índice de masa corporal es: " + str(my_data['IMC'][cont]) + " " + my_data['Nombre'][cont])
    
    cont += 1
    

print("\n------------------------------- EJERCICIO 2 -----------------------------\n")

# EJERCICIO 2

## A partir de los datos recolectados: Escribir un programa que teniendo en
## cuenta una cantidad a invertir, el interés anual y el número de años,
## muestre por pantalla el capital obtenido en la inversión.

#Recibimos nuestros datos del dataFrame, y armamos nuestra fórmula 

capitalFinal = my_data['Dinero a invertir']*((my_data['Interes anual']/100+1)**my_data['Años de inversión'])

#Una vez calculados nuestros valores, pasamos a mostrarlos

print("El capital obtenido en la inversión es: ")

print(capitalFinal)

print("\n------------------------------- EJERCICIO 3 -----------------------------\n")

# EJERCICIO 3

## Una panadería vende barras de pan a $15,000 COP cada una. El pan
## tiene un descuento del 10%, 20%, 30%, 40%, cuando no se vende en las
## primeras 6h, 12h, 18h, 24h, después de horneado. Crear una columna
## en el DataFrame para determinar el porcentaje de descuento obtenido
## de acuerdo a la hora en que fue realizada la compra. Y otra columna
## para el precio final obtenido.

precPan = 15000

cal = my_data['Hora Compra']

def calcularDescuento (cal):
    
    des = 0
    
    if (cal <= 6):
        des = precPan * 0.1
        return des
    
    elif (cal > 6) & (cal <= 12):
         des = precPan * 0.2
         return des
    
    elif (cal > 12) & (cal <=18):
        des = precPan * 0.3
        return des
    
    else:
        des = precPan * 0.4
        return des
    
my_data['Descuento'] = my_data['Hora Compra'].apply(calcularDescuento)
my_data['Precio_final'] = precPan - my_data['Descuento'] 


    #metodo que permite calcular el porcentaje de descuento de cada cliente
 #   def Descuento_Pan(self):
        
  #      condicion=[
   #                (self.datos["Hora de compra del pan"]<= 6),
    #               (self.datos["Hora de compra del pan"]> 6)&(self.datos["Hora de compra del pan"]<= 12),
      #             (self.datos["Hora de compra del pan"]> 12)&(self.datos["Hora de compra del pan"]<= 18),
     #              (self.datos["Hora de compra del pan"]> 18)&(self.datos["Hora de compra del pan"]<= 24)
                  
                  
                   #]
     
       # opcion =[0.10,
        #         0.20,
         #        0.30,
          #       0.40
           #     ]
        
        #self.datos["descuento"]= np.select(condicion,opcion)
    
    # metodo que permite calcular el valor de cada pan segun el descuento obtenido anterior mente el metodo anterior  
    #def Precio_Pan(self):
        
     #   self.datos["Percio Pan"]= 15000-(self.datos["descuento"]*15000)

print("\n------------------------------- EJERCICIO 4 -----------------------------\n")

## Los teléfonos de sus compañeros tienen el siguiente formato prefijonúmero-extensión donde el prefijo es el código del país +57, y la
## extensión tiene dos dígitos (por ejemplo +57-913724710-##). Debe
## organizar en el DataFrame (nueva columna) las extensiones de forma
## que si el sexo de la persona es M, debe poner como extensión 11 y si el
## sexo es F, debe poner como extensión 10.

#Creamos nuestra función encargada de las columnas para guardar nuestras extensiones

def extension(sexo):
    
    #Seguimos con nuestros condicionales
    
    if sexo == "Masculino":
        return 11
    
    elif sexo == "Femenino":
        return 10
    
    #Aplicamos los cambios
    
my_data["Ext_Num"] = my_data['Sexo'].apply(extension)   

n_numext = len(my_data['Ext_Num']) 

#Hacemos una variable contador, la cual nos llevará usaremos más adelante 

cont = 0
    
#Hacemos nuestro ciclo para imprimir el número de teléfono, y la extensión de cada uno

while cont < n_numext:
    
    print("+" + my_data['Numero de telefono'][cont] + " - " + str(my_data['Ext_Num'][cont]))
    
    cont += 1

