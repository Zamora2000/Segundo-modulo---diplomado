# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 23:46:11 2022

@author: Alvaro Zamora

# Alvaro José Zamora Cury
# identificación: 1003064557
# celular:3016842661
# correo: alvaro.zamora@upb.edu.co
# ID: 502225
# Taller #4, segundo módulo

"""

from sklearn import linear_model 
from scipy import stats
import pandas as pd
import numpy as np


# Primero convertimos el archivo cars.csv a DataFrame, para así poder acceder a su contenido

cars_df = pd.read_csv('cars.csv')

bus = []
cond = []
predicion_Car = 0

# Creamos nuestro método predicciónCO2, nos permitirá predecir la predicción de dicha emisión según su volumen de motor y peso del carro

def PredicionCO2(self,volumen, peso):
    
        x = self.cars_df[['Volume','Weight']]
        y = self.cars_df['CO2']
        
        x1= np.array(x)
        y1= np.array(y)
        
        reg_mod = linear_model.LinearRegression()
        reg_mod.fit(x1,y1)
        
        predic_co2 = reg_mod.predict([[volumen,peso]])
        
        print(predic_co2)
        
        print(reg_mod.coef_)
        
        
# Creamos nuestro método para ajustar los strings y reemplazar por números respectivamente etiquetados

def Etiquetar_Numerica_Car(self):
               
        marcas=self.cars_df["Car"]

        for dato in  marcas:

            if self.bus.count(dato) == 0 :
                self.bus.append(dato)

        etiqueta = range(len(self.bus))
    
        
        for dato_marca in self.bus:
                
            self.cond.append((self.cars_df["Car"]== dato_marca))
            
        self.cars_df["Car"]= np.select(self.cond,etiqueta)
        
        
# Nuestro método nos permite a través de valores independientes como (volumen, peso y producción de CO2) predecir el comportamiento de la variable dependiente

def Predicion_Car(self, x, y ,volumen,peso,co2):
        
        
        x1 = np.array(x)
        y1 = np.array(y)
        
        reg_mod = linear_model.LinearRegression()
        reg_mod.fit(x1,y1)
        
        predic_Car = reg_mod.predict([[volumen,peso,co2]])
        self.predicion_Car= round(predic_Car[0])
        
        print(predic_Car)
        
        print(reg_mod.coef_)
        
        
def Valor_R(self,Volume,Weight,Co2,Car):
        
        slope,intercept,r,p,std_err = stats.linregress(Volume,Car)
        slope1,intercept1,r1,p1,std_err1 = stats.linregress(Weight,Car)
        slope2,intercept2,r2,p2,std_err2 = stats.linregress(Co2,Car)
    
        return r,r1,r2
        
       


#Predicion = Regrecion()

print ("-------------------------Predicion  CO2-------------------------------------\n")
PredicionCO2(1300,2300)
Etiquetar_Numerica_Car()


print ("------------------------Predicion  Car--------------------------------------\n")
x = cars_df[['Volume','Weight','CO2']]
y = cars_df['Car']
Predicion_Car(x,y,1300,2000,107.20)


print ("------------------------Marca predecida--------------------------------------\n")

print (bus[predicion_Car])


print ("------------------------Valor de los R--------------------------------------\n")
volume1=list(cars_df['Volume'])
weight1=list(cars_df['Weight'])
co21=list(cars_df['CO2'])
car1=list(cars_df['Car'])
r,r1,r2 = Valor_R(volume1,weight1,co21,car1)
print ("R de correlación de la variable Volume con Car:  "+str(r))
print("R de correlación de la variable Weight con Car:  "+str(r1))
print("R de correlación de la variable CO2 con Car:  "+str(r2))


print ("------------------------Promedio de  R--------------------------------------\n")
print( "Promedio de R :"+str(np.median(Valor_R(volume1,weight1,co21,car1))))

