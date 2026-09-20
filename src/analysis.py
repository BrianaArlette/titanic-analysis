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

# Creación de nuevas variables
# ---------------------------

print("\n3. NUEVAS VARIABLES")

# FamilySize calcula cuántas personas de la familia viajaban juntas.
# Se suma 1 porque también se debe contar al propio pasajero.
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# A partir de FamilySize se identifica si viajaba solo o acompañado.
df["TravelStatus"] = df["FamilySize"].apply(
    lambda x: "Solo" if x == 1 else "Acompañado"
)

# Se agrupan las edades en categorías para poder compararlas más fácilmente.
def age_category(age):
    if age < 13:
        return "Niño"
    elif age < 18:
        return "Joven"
    elif age < 60:
        return "Adulto"
    else:
        return "Adulto mayor"


df["AgeGroup"] = df["Age"].apply(age_category)

# Se muestran las primeras filas para comprobar las nuevas variables.
print("\nEjemplo de las nuevas variables:")
print(
    df[
        ["Age", "FamilySize", "TravelStatus", "AgeGroup", "CabinKnown"]
    ].head()
)


# Análisis de los datos
# ---------------------

print("\n4. ANÁLISIS DE LOS DATOS")

# Análisis 1: porcentaje general de supervivencia.
# Survived utiliza 1 para sobreviviente y 0 para no sobreviviente,
# por eso su promedio multiplicado por 100 da el porcentaje.
survival_percentage = df["Survived"].mean() * 100

print("\nANÁLISIS 1: ¿Qué porcentaje de pasajeros sobrevivió?")
print(f"Porcentaje de supervivencia: {survival_percentage:.2f}%")


# Análisis 2: porcentaje de supervivencia según sexo.
survival_by_sex = df.groupby("Sex")["Survived"].mean() * 100

print("\nANÁLISIS 2: Supervivencia según sexo:")
print(survival_by_sex.round(2))


# Análisis 3: porcentaje de supervivencia según la clase del pasajero.
survival_by_class = df.groupby("Pclass")["Survived"].mean() * 100

print("\nANÁLISIS 3: Supervivencia según clase:")
print(survival_by_class.round(2))


# Análisis 4: porcentaje de supervivencia de cada grupo de edad.
survival_by_age = df.groupby(
    "AgeGroup", observed=False
)["Survived"].mean() * 100

print("\nANÁLISIS 4: Supervivencia según grupo de edad:")
print(survival_by_age.round(2))


# Análisis 5: comparación entre pasajeros que viajaban solos y acompañados.
survival_by_travel = df.groupby(
    "TravelStatus"
)["Survived"].mean() * 100

print("\nANÁLISIS 5: Supervivencia al viajar solo o acompañado:")
print(survival_by_travel.round(2))