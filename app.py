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

print(ListOfPopulations(ds))

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
    plt.hist(x=dataset[dataset['level5'] == city]["price"], ec = "black", label="Precio")
    plt.title(f"Precios de {city}")
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