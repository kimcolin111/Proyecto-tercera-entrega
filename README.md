[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5979974&assignment_repo_type=AssignmentRepo)
# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<nombre del autor\>   uvus:\<uvus del autor\>

Aquí debes añadir la descripción del dataset y un enunciado del dominio del proyecto.


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<modulo1.py\>**: Se trata de una lista de tuplas que almacena los datos del archivo csv.
  * **\<modulo1_test.py\>**: Se tratan de varias funciones que demuestran los datos guardados de diversas     formas.
  * **\<modulo2.py\>**: Añade descripciones para el resto de módulos que pueda tener tu proyecto. Por ejemplo, sería conveniente tener un módulo separado con funciones genéricas para dibujar gráficas y/o otro con funciones genéricas de conversión de tipos. 
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<dataset1.csv\>**: Se trata de un archivo csv que contiene información sobre varias series de netflix como: su titulo, director , fecha de estreno ,etc.
    * **\<dataset2.csv\>**: Añade una descripción del resto de datasets que puedas tener.
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<12\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<int\>, ID del programa
* **\<columna 2>**: de tipo \<str\>, El tipo de programa del que se trata.
* **\<columna 3>**: de tipo \<str\>, El titulo de la obra.
* **\<columna 4>**: de tipo \<str\>, El nombre del director.
* **\<columna 5>**: de tipo \<str\>, Los nombres del elenco.
* **\<columna 6>**: de tipo \<str\>, El pais del que poviene la pelicula.
* **\<columna 7>**: de tipo \<date\>, La fercha en la que se estrenó en netflix.
* **\<columna 8>**: de tipo \<date\>, La fecha en la que se realizó la serie.
* **\<columna 9>**: de tipo \<str\>, Aundiencia del programa.
* **\<columna 10>**: de tipo \<int\>, duracion de la serie.
* **\<columna 11>**: de tipo \<str\>, Los generos de la serie.
* **\<columna 12>**: de tipo \<str\>, descripción de la serie.
....

## Tipos implementados

Descrbe aquí la o las namedtuple que defines en tu proyecto.

DatosNetflix: se trata de una tupla que adjunta los datos con su colunma correspondiente.

## Funciones implementadas
Añade aquí descripciones genéricas de las funciones, que luego debes acompañar con comentarios de tipo documentación en el código

### \<modulo 1\>

* **<funcion 1>**: lee_datos_netflix(fichero): Esta función se encarga de almacenar los datos del archivo csv en una lista de tuplas.
* **<funcion 2>**: numero_paises_distintos(registros): Esta función se encarga de contar el numero de paises distintos que aparecen en el csv.
* **<funcion 3>**: suma_total_duracion(): Esta finción se encarga de sumar la duración en minutos de todos los datos del csv.
* **<funcion 4>**: maxima_duracion(): Esta función se encatrga de mostrar cunto dura la pelicula de maxima duración del csv.
* **<funcion 5>**: ordenar_por_duracion(minutos): Esta finción se encarga de ordenar los datos de menor a mayor si su duración es mayor a la que hemos indicado. 
* **<funcion 6>**:
* **<funcion 7>**:

### \<test modulo 1\>

* **<test funcion 1>**: print(len(datos_netflix)): Muestar en la pantalla el numero de elementos pertenecientes a la lista de tuplas.
* **<test funcion 2>**: print(datos_netflix[:3]): Muestara en pantalla las tres primeras lineas del la lista.
* **<test funcion 3>**: print(datos_netflix[-3:]): Muestara en pantalla las tres ultimas lineas del la lista.
* **<test funcion 4>**: print(numero_paises_distintos(datos_netflix)): Nos muestra el número de paises distintos.
* **<test funcion 5>**: print(suma_de_duracion_total(datos_netflix)): Suma la duración de todas las series y peliculas de netflix.
* **<test funcion 6>**: maxima_duracion(datos_netflix): Muestra la película de maxima duracion del csv.
* **<test funcion 7>**:print(ordenar_por_duracion(datos_netflix)): Ordena las series según su duración de menor a mayor.
* **<test funcion 8>**: print(diccionario(datos_netflix)): Crea un diccionario con el que consultar los datos del csv para asignar las peliculas producidas por cada país o serie de paises.
* **<test funcion 9>**: contador_apariciones_distrito(registros): Crea unos dicionarios que cuentan el número de peliculas por cada año.
* **<test funcion 10>**: 
* **<test funcion 11>**: 

### \<modulo 2\>

* **<funcion 1>**: Descripción de la función 1.
* **<funcion 2>**: Descripción de la función 2.
* ...
