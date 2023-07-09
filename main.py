from fastapi import FastAPI
import pandas as pd
df=pd.read_csv(r"movie_data.csv")
data=pd.read_csv(r"movie_credits.csv")

app=FastAPI()

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma):
    lista=df['original_language'].tolist()
    cantidad=0
    for item in lista:
        if item == idioma:
            cantidad+=1
    return {'Idioma':idioma, 'Cantidad':cantidad}


@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion( Pelicula: str ):
    lista=df['title'].tolist()
    indice=lista.index(Pelicula)
    duracion=df['runtime'][indice]
    anio=df['release_year'][indice]
    return {'Duracion':duracion, 'Año':anio}

@app.get('/franquicia/{franquicia}')
def franquicia( Franquicia: str ):
    collection=df['belongs_to_collection'].tolist()
    monto=df['revenue'].tolist()
    lista=[]
    for indice,elemento in enumerate(collection):
        if elemento == Franquicia:
            ganancia=int(monto[indice])
            lista.append(ganancia)
            ganancia_total=sum(lista)
            ganancia_promedio=ganancia_total/(len(lista))
    peliculas=len(lista)
    return ({'franquicia':Franquicia, 'cantidad':peliculas, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio})

@app.get('/peliculas_pais/{pais}')
def peliculas_pais( Pais: str):
    paises=df['production_countries'].tolist()
    contador=0
    for indice, elemento in enumerate(paises):
            if elemento == Pais:
                contador+=1
    return {'pais':Pais, 'cantidad':contador}

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas( Productora: str ):
    productoras=df['production_companies'].tolist()
    ganancia=df['revenue'].tolist()
    lista=[]
    for indice,elemento in enumerate(productoras):
        if elemento == Productora:
            valor=ganancia[indice]
            lista.append(valor)
    revenue_total=sum(lista)
    cantidad=len(lista)
    return {'productora':Productora, 'revenue_total': revenue_total,'cantidad':cantidad}


@app.get('/get_director/{nombre_director}')
def get_director(nombre_director:str):
    dir=data['crew']
    peli_lista=data['title'].tolist()
    año_lista=data['release_year'].tolist()
    retorno_lista=data['return'].tolist()
    budget_lista=data['budget'].tolist()
    revenue_lista=data['revenue'].tolist()
    #creo listas de las columnas del dataframe que utilizare 
    nuevo=[]
    nuevo1=[]
    nuevo2=[]
    nuevo3=[]
    nuevo4=[]
    #recorro la columan de directores y busco la coincidencia de el string ingresado por el ususario
    for indice,valor in dir.items():
        if valor == nombre_director:
            pelicula=peli_lista[indice]
            año=año_lista[indice]
            retorno=retorno_lista[indice]
            budget=budget_lista[indice]
            revenue=revenue_lista[indice]
    #agrego las coincidencias en varias listas
            nuevo.append(pelicula)
            nuevo1.append(año)
            nuevo2.append(retorno)
            nuevo3.append(budget)
            nuevo4.append(revenue)
    #se procede a concatenar las listas en una
    result = list(zip(nuevo,nuevo1,nuevo2,nuevo3,nuevo4))
    retorno_total=sum(nuevo2)
    user_keys=['title','anio', 'retorno','budget','revenue']
    resultado=[]
    resultado.append({'director': nombre_director, 'retorno_total':retorno_total })
    for user in result:
    #Agrego el diccionario al final de la lista resultado
        resultado.append(dict(zip(user_keys, user)))
    return(resultado)

    