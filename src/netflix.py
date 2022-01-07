import csv
from collections import namedtuple
from matplotlib import pyplot as plt
DatosNetflix = namedtuple('DatosNetflix', 'show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description')


def lee_datos_netflix(fichero):
    registros = []
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description in lector:
            show_id = float(show_id)
            country = str(country)
            release_year = int(release_year)
            semi_duration = duration.replace(" min", "")
            casi_duration = semi_duration.replace(" Season","")
            final_duration = casi_duration.replace("s","")
            final_duration = int(final_duration)
            tupla = DatosNetflix(show_id,type,title,director,cast,country,date_added,release_year,rating,final_duration,listed_in,description)
            registros.append(tupla)
        return registros
#2

def numero_paises_distintos(registros):
    conj = set(registro.country for registro in registros)
    return len(conj)
#3    
def suma_total_duracion(registros):
    lista_suma=[] 
    for final_duration in registros:
        lista_suma = [int(final_duration) for show_id,type,title,director,cast,country,date_added,release_year,rating,final_duration,listed_in,description in registros]
    suma=sum(lista_suma)
    return  suma
#5
def maxima_duracion(registros):
    for final_duration in registros:
       lista_max = [int(final_duration) for show_id,type,title,director,cast,country,date_added,release_year,rating,final_duration,listed_in,description in registros]
    maximo=max(lista_max)
    return maximo
#6
def ordenar_por_duracion(minutos):
    datos = lee_datos_netflix('data/netflix_titles.csv')
    lista_orden = [(float(show_id),type,title,director,cast,country,date_added,release_year,rating,int(final_duration),listed_in,description) for show_id,type,title,director,cast,country,date_added,release_year,rating,final_duration,listed_in,description in datos if final_duration >= minutos]
    lista_orden.sort(key = lambda x: x[9])
    return lista_orden
#7
def diccionario(registros):
    res={}
    for registro in registros:
        clave = registro.country
        if clave not in res:
            res[clave]= set(registro.title)
        else:
            res[clave].add(registro.title)    
    return res
#8
def contador_peliculas_año(registros):
    contador={}
    for release_year in set([r.release_year for r in registros]):
        contador[release_year]=len(set([r.listed_in for r in registros if r.release_year == release_year and r.type == 'Movie']))
    return contador
#11
'''
    Children & Family Movies 
    Comedies
    Kids
    Crime TV Shows 
    International TV Shows 
    Spanish-Language TV Shows
    International Movies 
    Sci-Fi & Fantasy 
    Thrillers
    Docuseries 
    Science & Nature TV
    Action & Adventure
    Dramas
    Independent Movies
    Romantic Movies
    Horror Movies
'''
#12
def contador_duracion_peliculas_año(registros):
    lista_duracion = []
    lista_duracion = []
    diccionario = {}
    for i in registros:
        lista_duracion.append(i.release_year)
    for d in registros:
        lista_duracion.append(d.duration)
    diccionario['release_year' , 'duration'] = max(lista_duracion), max(lista_duracion)
    return diccionario
        
#14
def funcion_14(registros, n):
    lista_generos = []
    lista_duracion = []
    diccionario2 = {}
    for i in registros:
        lista_generos.append(i.release_year)
    for d in registros:
        lista_duracion.append(d.duration)
    diccionario2['release_year' , 'duration'] = sorted(lista_generos, reverse=True)[:n], sorted(lista_duracion,reverse=True)[:n]
    return diccionario2
 
#gráfica
def grafica(registros):
    contador = {}
    contador = contador_peliculas_año(registros)
    x = list(contador.keys())
    y = list(contador.values())
    plt.bar(x,y)
    plt.xticks(size= 'small' , rotation= 90)
    plt.show()
