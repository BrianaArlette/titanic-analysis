# Análisis de pasajeros del Titanic

## Descripción del proyecto

Este proyecto realiza un análisis exploratorio y preprocesamiento de los datos de los pasajeros del Titanic. Se analizan diferentes características de los pasajeros con el objetivo de identificar patrones relacionados con la supervivencia.

No se realiza ningún modelo de Machine Learning.

## Dataset

**Nombre:** Titanic - Machine Learning from Disaster  
**Fuente:** Kaggle  
**Archivo utilizado:** train.csv

El dataset contiene información de los pasajeros del Titanic, incluyendo variables como edad, sexo, clase del pasajero, tarifa pagada, número de familiares y supervivencia.

## Objetivo

Analizar la información disponible de los pasajeros del Titanic mediante limpieza, preprocesamiento, análisis exploratorio y visualizaciones para identificar características asociadas con la supervivencia.

## Requisitos

Para ejecutar este proyecto se requiere:

- Python
- Git
- Las dependencias incluidas en `requirements.txt`

Las principales bibliotecas utilizadas son:

- pandas
- matplotlib

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/BrianaArlette/titanic-analysis.git
```

Entrar a la carpeta del proyecto:

```bash
cd titanic-analysis
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el análisis:

```bash
python src/analysis.py
```

Los resultados y las gráficas generadas se guardan en la carpeta `outputs`.

## Limpieza y preprocesamiento

Se realizó una revisión inicial de los datos para identificar valores faltantes, registros duplicados, tipos de datos y estadísticas descriptivas.

Para los valores faltantes se tomaron las siguientes decisiones:

- **Age:** los valores faltantes se sustituyeron por la mediana para reducir el efecto de valores extremos y conservar los registros.
- **Embarked:** los valores faltantes se sustituyeron por la moda, es decir, el puerto de embarque más frecuente.
- **Cabin:** debido a la gran cantidad de datos faltantes, no se asignaron cabinas inexistentes. En su lugar, se creó la variable `CabinKnown` para indicar si se conoce o no la cabina.

## Nuevas variables

Se crearon las siguientes variables para ampliar el análisis:

- **FamilySize:** representa el tamaño de la familia que viajaba junta.
- **TravelStatus:** indica si el pasajero viajaba solo o acompañado.
- **AgeGroup:** agrupa a los pasajeros en niño, joven, adulto y adulto mayor.
- **CabinKnown:** indica si existe información de la cabina del pasajero.

## Análisis realizados

Se analizaron los siguientes aspectos:

1. Porcentaje general de pasajeros que sobrevivieron.
2. Supervivencia según sexo.
3. Supervivencia según clase del pasajero.
4. Supervivencia según grupo de edad.
5. Supervivencia de pasajeros que viajaban solos o acompañados.

## Visualizaciones

Se generaron cuatro gráficas:

- Supervivencia según sexo.
- Supervivencia según clase.
- Supervivencia según grupo de edad.
- Supervivencia de pasajeros que viajaban solos o acompañados.

Las gráficas se guardan automáticamente en la carpeta `outputs`.

## Conclusiones

El análisis permite observar diferencias en los porcentajes de supervivencia según distintas características de los pasajeros. En los datos analizados, las mujeres presentan un mayor porcentaje de supervivencia que los hombres y también se observan diferencias según la clase, el grupo de edad y si el pasajero viajaba solo o acompañado.

Los resultados muestran asociaciones presentes en el dataset y no implican necesariamente relaciones de causa y efecto.