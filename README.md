[![Typing SVG](https://readme-typing-svg.demolab.com?font=Alfa+Slab+One&size=35&pause=1000&color=F7A2CE&vCenter=true&width=435&lines=Proyecto+Final+Markov)](https://git.io/typing-svg)

---
### Proyecto final de la materia Procesos Estocásticos

# Cadenas de Markov para Generación de Texto 🎶📜

---
## 🎯 Objetivo del Proyecto

El objetivo es modelar un texto palabra por palabra usando una **Cadena de Markov de primer orden**, donde la aparición de una palabra depende únicamente de la palabra anterior. A partir de un corpus de letras de canciones, construimos:

- Un **vocabulario** (espacio de estados).
- Una **matriz de transiciones** basada en frecuencias de pares de palabras.
- Funciones para **análisis** (clases de comunicación, periodicidad, probabilidades a \( n \)-pasos).
- Una herramienta para **generar texto** simulando la cadena.

El resultado es un sistema que genera secuencias de texto similares al estilo del corpus, junto con un análisis profundo de las propiedades de la cadena. 📊🎸

---
## 📚 Descripción del Corpus

### 🎵 Elección del Corpus
Seleccionamos un corpus de **letras de canciones en español**, principalmente del género **rock y pop latinoamericano**, con artistas icónicos como:

- **Soda Stereo** 
- **Héroes del Silencio** 
- **Fito Páez** 
- **Charly García** 
- **Los Fabulosos Cadillacs**, entre otros.

**Razón de la elección**:
- Las letras de rock/pop en español son ricas en vocabulario y estructuras poéticas, ideales para modelar transiciones de palabras.
- La diversidad de artistas asegura un corpus variado pero cohesionado en estilo.
- Las canciones tienen una longitud adecuada (mínimo 200 palabras por texto) y son accesibles a través de la API de **Genius**.

El corpus final incluye **53 canciones** con un total de **14,533 palabras** y un vocabulario de **2,391 palabras únicas**. 📝

---
## 🛠️ Estructura del Proyecto

El proyecto está organizado en varios archivos clave:

### 1. **`PF-ScriptLetras.py`**
   - **Propósito**: Descarga, preprocesa y guarda las letras de canciones desde la API de Genius.
   - **Funcionalidades**:
     - Conecta con la API de **Genius** usando un token.
     - Descarga letras de una lista predefinida de canciones.
     - Normaliza el texto (minúsculas, sin acentos, elimina puntuación, metadatos, etc.).
     - Filtra canciones con menos de 200 palabras.
     - Guarda las letras normalizadas en archivos `.txt` en la carpeta `corpus/`.
   - **Librerías usadas**: `lyricsgenius`, `nltk`, `unidecode`, `re`, `os`.

### 2. **`PF-Analisis.ipynb`**
   - **Propósito**: Implementa el modelo de Cadena de Markov, análisis y visualización.
   - **Funcionalidades**:
     - Carga y preprocesa el corpus desde la carpeta `corpus/`.
     - Construye el **vocabulario** (palabras únicas).
     - Calcula la **distribución inicial** (frecuencia de palabras).
     - Genera la **matriz de transiciones** basada en frecuencias de pares de palabras.
     - Realiza análisis de:
       - **Clases de comunicación** usando componentes fuertemente conectados.
       - **Periodicidad** de estados.
       - **Probabilidades a \( n \)-pasos** con las ecuaciones de Chapman-Kolmogorov.
     - Genera texto simulado a partir de una palabra inicial.
     - Visualiza la distribución inicial y un subgrafo de transiciones.
   - **Librerías usadas**: `numpy`, `pandas`, `matplotlib`, `seaborn`, `networkx`, `collections`.

### 3. **`Proyecto Cadenas de Markov.pdf`**
   - **Propósito**: Documento con las instrucciones y rúbrica del proyecto.
   - **Contenido**:
     - Objetivos, descripción de la aplicación, requisitos del corpus.
     - Especificaciones de implementación (procesamiento, modelo, análisis).
     - Requisitos del informe escrito y presentación oral.
     - Rúbrica de evaluación.

### 4. **Carpeta `corpus/`**
   - Contiene los archivos `.txt` con las letras normalizadas de las canciones.

---
## 🚀 Instrucciones de Uso

### 📋 Requisitos
Asegúrate de tener instalado **Python 3.8+** y las siguientes librerías:

```bash
pip install lyricsgenius nltk unidecode numpy pandas matplotlib seaborn networkx
```

Además, se necesita un **token de acceso** de la API de Genius. Regístrate en [Genius](https://genius.com/api-clients) y para obtener uno.

### 🛠️ Configuración

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Titolin4612/PF-ProcesosEstocasticos.git
   cd PF-Markov
   ```

2. **Configura el token de Genius**:
   - Abre `PF-ScriptLetras.py`.
   - Reemplaza el token en la línea:
     ```python
     genius = lyricsgenius.Genius('TU_TOKEN_AQUÍ', timeout=15)
     ```
   - Guarda los cambios.

3. **Crea la carpeta para el corpus**:
   - Asegúrate de que la carpeta `corpus/` exista en la ruta especificada:
     ```python
     output_dir = r"C:\ruta\a\tu\carpeta\corpus"
     ```
   - Actualiza la ruta si es necesario en `PF-ScriptLetras.py` y `PF-Analisis.ipynb`.

### 🎵 Descarga del Corpus
1. Ejecuta `PF-ScriptLetras.py` para descargar y normalizar las letras:
   ```bash
   python PF-ScriptLetras.py
   ```
2. Esto creará archivos `.txt` en la carpeta `corpus/` con las letras normalizadas.

### 📊 Análisis y Generación de Texto
1. Abre `PF-Analisis.ipynb` en **Jupyter Notebook**:
   ```bash
   jupyter notebook PF-Analisis.ipynb
   ```
2. Ejecuta las celdas en orden para:
   - Cargar el corpus.
   - Construir el vocabulario y el modelo de Markov.
   - Analizar clases de comunicación, periodicidad y probabilidades.
   - Generar texto simulado.
   - Visualizar resultados (histogramas, grafos).

### 📝 Personalización
- **Cambiar el corpus**: Modifica la lista `canciones` en `PF-ScriptLetras.py` para incluir otras canciones o artistas.
- **Ajustar parámetros**:
  - Cambia el umbral de palabras mínimas (200) en `PF-ScriptLetras.py`.
  - Ajusta el tamaño del subgrafo en `PF-Analisis.ipynb` para visualización.

---
## 🌈 Resultados Esperados

### 📈 Visualizaciones
- **Histograma de la distribución inicial**: Muestra las palabras más frecuentes (e.g., "que", "de", "la").
- **Grafo de transiciones**: Visualiza un subgrafo con las palabras más comunes y sus probabilidades de transición.

### 🔍 Análisis
- **Clases de comunicación**: Identifica si el subgrafo es irreducible o reducible.
- **Periodicidad**: Determina si los estados son aperiódicos o periódicos.
- **Probabilidades a \( n \)-pasos**: Calcula la probabilidad de transiciones tras \( n \) pasos usando Chapman-Kolmogorov.

### 🎤 Texto Generado
El modelo genera secuencias de texto que imitan el estilo del corpus. Ejemplo:
```
que no te quiero amor de la noche ...
```
Aunque no siempre son coherentes, reflejan patrones del rock/pop en español.

---

