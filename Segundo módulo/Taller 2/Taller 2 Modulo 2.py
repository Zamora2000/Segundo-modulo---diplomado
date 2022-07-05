# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 22:59:38 2022

@author: Alvaro Zamora

# Alvaro José Zamora Cury
# identificación: 1003064557
# celular:3016842661
# correo: alvaro.zamora@upb.edu.co
# ID: 502225
# Taller #2, segundo módulo

"""

# Lea la base de datos netflix_titles usando la librería “pandas”.

import pandas as pd 

my_nexflix = pd.read_csv('netflix_titles.csv')

# Imprima por consola las primeras y últimas 5 filas del arreglo.

# Primeras 5 filas
print(my_nexflix.head(5))

# Últimas 5 filas
print(my_nexflix.tail(5))

##Imprima cada uno de los tipos de dato asociado a las etiquetas

print(my_nexflix.dtypes)

# Guarde un archivo .xlsx, en el cual el nombre del archivo sea “Netflix_list” y el nombre de la hoja sea “títulos”.

my_nexflix.to_excel("Netflix_list.xlsx", sheet_name="títulos", index=False)

# Cree una nueva data frame en el cual segmente únicamente: el tipo, la duración, la descripción y el país.

new_data_nexflix = my_nexflix.loc[:,['type','duration','description','country']]

# Haga un filtro para las películas que tienen una duración superior a 100 min.

my_nexflix["duration_minutos"] = pd.to_numeric(my_nexflix['duration'].replace('([^0-9]*)','', regex=True), errors='coerce')

filtro_duracion = my_nexflix[my_nexflix["duration_minutos"] > 100]

# Haga un filtro para los “TV Shows” que tienen más de 3 temporadas.

filtro_Tv_shows= my_nexflix[my_nexflix["type"] == "TV Show"]

# Haga un filtro en el cual solo tenga en cuenta 2 categorías/etiquetas (libre elección).

Categorias = my_nexflix.loc[my_nexflix['country'].isin(['India','Germany, Czech Republic'])]

# Recuerde usar casos con indexación numérica y con texto (loc / iloc).

# Modifique los valores del ID de las 5 primeras y las 5 últimas “shows” y de cualquier otra etiqueta de su elección (solo un valor)

my_nexflix.iloc[:5,0]='s10'

my_nexflix.iloc[8802:,0]='s1'

