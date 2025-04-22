# NBA Predictor

Este es un proyecto que utiliza Machine Learning para predecir el ganador de un partido de la NBA, basándose en datos históricos de equipos. El modelo está entrenado con regresión logística y codificación One-Hot para predecir el ganador entre dos equipos seleccionados.

## 📊 Descripción

El modelo se entrenó usando un conjunto de datos con los resultados de partidos de la NBA, con las siguientes variables:
- **Home Team**: El equipo local.
- **Away Team**: El equipo visitante.

### Resultados
- **Precisión del modelo**: 0.39 (basado en un conjunto de datos de la temporada 2023).

El modelo predice el ganador basándose en la diferencia de puntos entre los equipos y los equipos involucrados.

## 🛠️ Tecnologías

- Python
- Flask
- scikit-learn
- joblib

## 💻 Requisitos

- Python 
- Las dependencias del proyecto se pueden instalar utilizando el archivo `requirements.txt`:
  
  ```bash
  pip install -r requirements.txt


tos:** Los datos de los partidos de la NBA fueron extraídos utilizando **web scraping** desde [Ba>

## 🚀 Instrucciones para ejecutar el proyecto

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/nba-predictor.git

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt

3. Ejecuta la aplicación Flask:

   ```bash
   python app/app.py

La aplicación estará disponible en http://127.0.0.1:5000.

## 🧠 Entrenamiento del Modelo

Para entrenar el modelo de predicción de resultados NBA se realizó lo siguiente:

1. **Selección de características:**
   Se eligieron las columnas `'Home Team'` y `'Away Team'` como variables de entrada (`X`), y la columna `'Winner'` como variable objetivo (`y`), que representa el equipo ganador de cada partido.

2. **Codificación de variables categóricas:**
   Como los equipos están representados por texto, se utilizó `OneHotEncoder` para convertirlos en variables numéricas. Esto se realizó con un `ColumnTransformer` que aplica la codificación solo a las columnas de equipo.

3. **Construcción del modelo:**
   Se creó un pipeline que integra el preprocesamiento (codificación) y un clasificador (`LogisticRegression`) en un solo flujo de trabajo, facilitando el entrenamiento y las predicciones.

4. **División del conjunto de datos:**
   Los datos se dividieron en un 80% para entrenamiento y un 20% para pruebas (`train_test_split`) para evaluar el rendimiento del modelo.

5. **Entrenamiento:**
   El modelo se entrenó usando los datos históricos de partidos.

6. **Evaluación:**
   Se calculó la precisión (`accuracy_score`) del modelo en los datos de prueba, obteniendo una precisión aproximada de **0.38**, lo que indica que aún hay espacio para mejorar el rendimiento del modelo con más datos o técnicas más complejas.

```python
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

