import pandas as pd

# Este archivo CSV contiene puntos y comas en lugar de comas como separadores
ds = pd.read_csv('assets/real_estate.csv', sep=';')
print (ds)

# Casa más cara de todo el dataset

def MoreExpensiveHouse(dataset):
    moreexpensivehouse = dataset.sort_values("price", ascending = False).head(1).squeeze()
    return f"La casa en {moreexpensivehouse['address']}, es la más cara y su precio es de {moreexpensivehouse['price']} €."

MoreExpensiveHouse(ds)

# Casa más barate del dataset

def LessExpensiveHouse(dataset):
    lessexpensivehouse = dataset.sort_values("price", na_position = "first").head(1).squeeze()
    return f"La casa con dirección en {lessexpensivehouse['address']}, es la más cara y su precio es de {lessexpensivehouse['price']}"

print (LessExpensiveHouse(ds))

# Casa más grande del dataset

def MoreSurfaceHouse(dataset):
    moresurfacehouse = dataset.sort_values("surface", ascending = False).head(1).squeeze()
    return f"La casa más grande está ubicada en {moresurfacehouse['address']} y su superficie es de {moresurfacehouse['surface']} metros."

print(MoreSurfaceHouse(ds))

# Casa más pequeña del dataset

def LessSurfaceHouse(dataset):
    lesssurfacehouse = dataset.sort_values("surface").head(1).squeeze()
    return f"La casa más pequeña está ubicada en {lesssurfacehouse['address']} y su superficie es de {lesssurfacehouse['surface']} metros."

print(LessSurfaceHouse(ds))

# Nombre de poblaciones que tiene el dataset.

def ListOfPopulations(dataset):
    listofpopulations = dataset["level5"].unique()
    return listofpopulations

for i in ListOfPopulations(ds):
    print(i, end=", ")

# Comprobar si el dataset contiene Na´s

def IdentifyNanValues(dataset):
    return dataset.isna().any(), dataset.isna().any(axis = 1)

print(IdentifyNanValues(ds))

# Eliminar Nas del dataset

def ClearDataset(dataset):
    deletedna = dataset.dropna(axis = 1, how="all").reset_index()
    meansurface = dataset["surface"].mean()
    narefill = deletedna.fillna(value = meansurface)
    return narefill

cleandataset = ClearDataset(ds)

print(cleandataset.shape)
print(ds.shape)

# Media de precios en Arroyomolinos (Madrid)

def MeanPricePopulation(dataset, city):
    return dataset[dataset['level5'] == city]["price"].mean()

print(MeanPricePopulation(cleandataset, "Arroyomolinos (Madrid)"))

# Histograma de los precios de la poblacion de Arroyomolinos

import matplotlib.pyplot as plt

def HistogramPopulation(dataset, city):
    plt.hist(dataset[dataset['level5'] == city]["price"], ec = "black", label= city)

HistogramPopulation(cleandataset, "Arroyomolinos (Madrid)")
plt.title("Arroyomolinos (Madrid)")
plt.legend()
plt.show()

print(HistogramPopulation(cleandataset, "Arroyomolinos (Madrid)"))

# Comprobar si el promedio de Valdemorillo y Galapagar son el mismo.

print(f"Galapagar: {MeanPricePopulation(cleandataset, 'Galapagar')}")
print(f"Valdemorillo: {MeanPricePopulation(cleandataset, 'Valdemorillo')}")
print (f"La conclusión sobre la igualdad de la media entre ambos pueblo es: {MeanPricePopulation(cleandataset, 'Galapagar') == MeanPricePopulation(cleandataset, 'Valdemorillo')}")

# Comprobar si el precio medio por metro cuadrado entre Valdemorillo y Galapagar es el mismo.

def PPSDataSet(dataset):
    pps = dataset["price"]/dataset["surface"]
    dataset["pps"] = pps
    return dataset

dscleanwithpps = PPSDataSet(cleandataset)

def MeanPPSPopulation(dataset, city):
    return dataset[dataset['level5'] == city]["pps"].mean()

print(f"Valdemorillo: {MeanPPSPopulation(dscleanwithpps, 'Valdemorillo')}")
print(f"Galapagar: {MeanPPSPopulation(dscleanwithpps, 'Galapagar')}")
print(f"La conclusión sobre la igualdad de la media de precio por metro cuadrado es: {MeanPPSPopulation(dscleanwithpps, 'Valdemorillo') == MeanPPSPopulation(dscleanwithpps, 'Galapagar')}")

# Analiza la relacion entre la superficie y el precio de las casas.

def RelationPriceSurface(dataset, city):
    return plt.scatter(x = dataset[dataset['level5'] == city]["price"], y = dataset[dataset['level5'] == city]["surface"], label = city, ec="black")

RelationPriceSurface(dscleanwithpps, "Valdemorillo")
RelationPriceSurface(dscleanwithpps, "Galapagar")
plt.legend()
plt.show()

# Número de agencias en el dataset

def NumberOfRealEstates(dataset):
    return len(dataset["realEstate_name"].unique())

print(NumberOfRealEstates(dscleanwithpps))

# Población con más cantidad de casas.

def MoreHousesPopulation(dataset):
    return dataset.value_counts("level5").head(1)
   

print(MoreHousesPopulation(dscleanwithpps))

# Creamos dataset del cinturon sur

def CinturonSur(dataset):
    cinturonsur = dataset[dataset["level5"].isin(["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"])].reset_index()
    cinturonsur.drop('index', axis = 1)
    return cinturonsur.drop('index', axis = 1)

cinturonsur = CinturonSur(dscleanwithpps)

print(cinturonsur)

# Grafica de barras con la MEDIANA de los precios de las ciudades.

def MedianPricePopulation(dataset, city):
    return dataset[dataset['level5'] == city]["price"].median()

plt.bar(["Fuenlabrada", "Leganés", "Alcorcón", "Getafe"], [(MedianPricePopulation(cinturonsur, "Fuenlabrada")), (MedianPricePopulation(cinturonsur, "Leganés")), (MedianPricePopulation(cinturonsur, "Getafe")), (MedianPricePopulation(cinturonsur, "Alcorcón"))], ec="black")
plt.title("Mediana de precios en Cinturon Sur")
plt.show()

# Calcula Media y varianza para precio, habitaciones, superficies y baños

def VarianceValuesCity (dataset, value):
    return dataset[value].var()

def MeanValuesCity(dataset, value):
    return dataset[value].mean()

print(f"La varianza en los precios es: {VarianceValuesCity(cinturonsur, 'price')}")
print(f"La media de los precios es : {MeanValuesCity(cinturonsur, 'price')}")
print(f"La varianza en las habitaciones es: {VarianceValuesCity(cinturonsur, 'rooms')}")
print(f"La media de las habitaciones es : {MeanValuesCity(cinturonsur, 'rooms')}")
print(f"La varianza en los metros es: {VarianceValuesCity(cinturonsur, 'surface')}")
print(f"La media de los metros es : {MeanValuesCity(cinturonsur, 'surface')}")
print(f"La varianza en los baños es: {VarianceValuesCity(cinturonsur, 'bathrooms')}")
print(f"La media de los baños es : {MeanValuesCity(cinturonsur, 'bathrooms')}")

# Casa más cara de cada población

def MoreExpensiveHouseInPopulation(dataset, city):
    moreexpensivehouseinpopulation = dataset[dataset['level5'] == city].sort_values("price", ascending = False).head(1).squeeze()
    return f"La dirección de la casa más cara es {moreexpensivehouseinpopulation['address']} y su precio es de {moreexpensivehouseinpopulation['price']} €."

print(MoreExpensiveHouseInPopulation(cinturonsur, "Fuenlabrada"))
print(MoreExpensiveHouseInPopulation(cinturonsur, "Getafe"))
print(MoreExpensiveHouseInPopulation(cinturonsur, "Alcorcón"))
print(MoreExpensiveHouseInPopulation(cinturonsur, "Leganés"))

