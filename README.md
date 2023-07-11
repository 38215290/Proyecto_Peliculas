# proyect_1
![image](https://github.com/38215290/proyect_1/assets/127343400/aec11a84-0c3c-4f52-b59d-eb5ffef22865)

*Machine Learning Operations (MLOps)*

![image](https://github.com/38215290/proyect_1/assets/127343400/a919f596-cca9-4203-ad00-fbf17b44caec)

Descripción del problema planteado :

Debemos crear un sistema de recomendaciones que recomienda peliculas segun las peliculas vistas por el usuario
Tenemos datos de películas y metadatos extraídos de plataformas de streaming que necesitamos transformar para obtener información relevante y permitir consultas a través de una API.

DICCIONARIO DE  DATOS
Característica | Descripcion
adulto: Indica si la película tiene calificación X, exclusiva para adultos.
Pertenece a la colección: Un diccionario que indica a que franquicia o serie de películas pertenece a la película
presupuesto: El presupuesto de la película, en dólares
géneros: Un diccionario que indica todos los géneros asociados a la película
homepage: La página web oficial de la película
id: ID de la pelicula
imdb_id: IMDB ID de la pelicula
original_language: Idioma original en la que se grabo la pelicula
original_title: Título original de la película
resumen: Pequeño resumen de la película
Popularidad: Puntaje de popularidad de la película, asignado por TMDB (TheMoviesDataBase)
poster_path: URL del póster de la película
production_companies: Lista con las compañias productoras asociadas a la pelicula
production_countries: Lista con los países donde se produjo la película
release_date: Fecha de estreno de la película
Revenue: Recaudación de la pelicula, en dolares
runtime: Duración de la película, en minutos
speak_languages: Lista con los idiomas que se hablan en la pelicula
status: Estado de la pelicula actual (si fue anunciada, si ya se estreno, etc)
Slogan: Frase célebre asociada a la pelicula
title: Título de la película
video: Indica si hay o no un trailer en video disponible en TMDB
vote_average: Puntaje promedio de reseñas de la pelicula
vote_count: Numeros de votos recibidos por la pelicula, en TMDB

En el siguiente proyecto muestra los pasos a seguir para obtener un MVP( Minimum Viable Product )  y con tal que debe ser una API que puede ser consumida  , por lo tanto se tuvo en cuenta  el siguiente proceso :

![image](https://github.com/38215290/proyect_1/assets/127343400/03a8653e-6d45-43a2-a21e-45f85e6f0214)

 En cada una de las etapas se tuvo en cuenta que el dataset deberia estar en condiciones para visualizarlo se adjunta el archivo EDA.ipynb para lograr levantar la API con las funciones requeridas :

 
 def peliculas_idioma( Idioma: str ) : Se ingresa un idioma (como están escritos en el dataset). Debe devolver la cantidad de películas producidas en ese idioma. 
 
                    Ejemplo de retorno: Xcantidad de peliculas fueron estrenadas enidioma

def peliculas_duracion( Pelicula: str ) : Se ingresa una pelicula. Debe devolver la duración y el año.

                    Ejemplo de retorno: X. Duración: x. Año:xx

def franquicia( Franquicia: str ) : Se ingresa la franquicia, regresando la cantidad de peliculas, ganancia total y promedio.

                    Ejemplo de retorno: La franquicia Xposee Xpeliculas, una ganancia total de xy una ganancia promedio dexx

def peliculas_pais( Pais: str ) : Se ingresa un país (como están escritos en el dataset), retornando la cantidad de peliculas producidas en el mismo.

                    Ejemplo de retorno: Se producen Xpelículas en el paísX

def productoras_exitosas( Productora: str ) : Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo.
                    Ejemplo de retorno: La productora Xha tenido un ingreso dex

def get_director( nombre_director) : Se ingresa el nombre de un director que se encuentra dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.
 

Luego implementado  los conocimientos necesarios  de machine learning se debera realizo una funcion donde a partir de la entrada de una variable de una pelicula retornara 5 peliculas similares a esta :

def recomendacion( titulo) : Se ingresa el nombre de una pelicula y te recomienda las similares en una lista de 5 valores.
 
