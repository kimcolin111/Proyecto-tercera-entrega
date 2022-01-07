from netflix import *

datos_netflix = lee_datos_netflix('data/netflix_titles.csv') 

print(len(datos_netflix))
print(datos_netflix[:3])

print(datos_netflix[-3:])
#2
print(numero_paises_distintos(datos_netflix))
#3
print(suma_total_duracion(datos_netflix), 'min')
#5
print(maxima_duracion(datos_netflix), 'min')
#6
print(ordenar_por_duracion(120))
#7
print(diccionario(datos_netflix))
#8
print(contador_peliculas_año(datos_netflix))
#11

#12
print(contador_duracion_peliculas_año(datos_netflix))
#14
print(funcion_14(datos_netflix, 3))
#gráfica
grafica(datos_netflix)