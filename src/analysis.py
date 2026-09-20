import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Proyecto: análisis de pasajeros del Titanic
# -------------------------------------------

# Se definen las rutas para poder leer el dataset y guardar los resultados
# sin depender de la ubicación exacta de la carpeta en la computadora.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "train.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

# Crea la carpeta outputs si todavía no existe.
# Si ya existe, exist_ok=True evita que se genere un error.
OUTPUT_DIR.mkdir(exist_ok=True)


# Carga del dataset
# -----------------

# Pandas lee el archivo CSV y lo guarda en un DataFrame llamado df.
df = pd.read_csv(DATA_PATH)


# Exploración inicial
# -------------------

# Primero se revisa la información general del dataset antes de modificarlo.
print("\n1. EXPLORACIÓN INICIAL DEL DATASET")

print("\nNúmero de pasajeros:")
print(df.shape[0])

print("\nNúmero de columnas:")
print(df.shape[1])

print("\nVariables disponibles:")
print(df.columns.tolist())

print("\nTipos de datos:")
print(df.dtypes)

# Se revisan los valores faltantes para saber qué columnas necesitan tratamiento.
print("\nValores faltantes por columna:")
print(df.isnull().sum())

# Se comprueba si existen filas completamente duplicadas.
print("\nRegistros duplicados:")
print(df.duplicated().sum())

# Muestra un resumen estadístico de las variables del dataset.
print("\nEstadísticas descriptivas:")
print(df.describe(include="all"))

# Limpieza y preprocesamiento
# --------------------------

print("\n2. LIMPIEZA Y PREPROCESAMIENTO")

# Age: se usa la mediana para completar las edades faltantes.
# La mediana se ve menos afectada por valores extremos que el promedio
# y permite conservar los registros que no tienen una edad registrada.
age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

# Embarked: se usa la moda porque representa el puerto de embarque
# que aparece con mayor frecuencia en el dataset.
embarked_mode = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(embarked_mode)

# Cabin tiene una gran cantidad de datos faltantes.
# En vez de inventar una cabina, se crea una variable que indica
# solamente si la información de la cabina está disponible.
df["CabinKnown"] = df["Cabin"].notna().map({True: "Sí", False: "No"})

print(f"\nMediana utilizada para completar Age: {age_median}")
print(f"Moda utilizada para completar Embarked: {embarked_mode}")

# Se vuelven a revisar estas columnas para comprobar el tratamiento realizado.
print("\nValores faltantes después del tratamiento:")
print(df[["Age", "Cabin", "Embarked"]].isnull().sum())