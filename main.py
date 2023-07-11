from fastapi import FastAPI
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
df=pd.read_csv(r"movie_credits.csv")

app=FastAPI()

@app.get("/")

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
    dir=df['crew']
    peli_lista=df['title'].tolist()
    año_lista=df['release_year'].tolist()
    retorno_lista=df['return'].tolist()
    budget_lista=df['budget'].tolist()
    revenue_lista=df['revenue'].tolist()
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

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    #filtro el dataset debido al almacenamiento que demanda por eso se tomo en cuentas las peliculas con votos mayores a 100
    filtro=df['vote_count'] > 100.0
    smd = df[filtro]
    peli=smd['title']
    count = CountVectorizer(analyzer='word',min_df=0.0, stop_words='english')
    count_matrix = count.fit_transform(peli)
    item_features = count_matrix
    cosine_sim = linear_kernel(item_features, item_features)
    smd = smd.reset_index()
    indices = pd.Series(df['title'].index, index=df['title'])
    idx = indices[titulo]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    resultado=peli.iloc[movie_indices].head(5)
    resultado.to_dict()
    return {'lista recomendada': resultado}