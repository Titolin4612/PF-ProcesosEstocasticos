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

<svg width="100%" height="100%" id="svg" viewBox="0 0 1440 590" xmlns="http://www.w3.org/2000/svg" class="transition duration-300 ease-in-out delay-150"><style>
          .path-0{
            animation:pathAnim-0 4s;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
          }
          @keyframes pathAnim-0{
            0%{
              d: path("M 0,600 L 0,0 C 117.87559808612443,32.248803827751196 235.75119617224885,64.49760765550239 317,80 C 398.24880382775115,95.50239234449761 442.87081339712915,94.25837320574163 537,93 C 631.1291866028708,91.74162679425837 774.7655502392345,90.46889952153111 870,110 C 965.2344497607655,129.5311004784689 1012.0669856459331,169.86602870813397 1099,155 C 1185.933014354067,140.13397129186603 1312.9665071770335,70.06698564593302 1440,0 L 1440,600 L 0,600 Z");
            }
            25%{
              d: path("M 0,600 L 0,0 C 86.29665071770336,45.39712918660287 172.59330143540672,90.79425837320574 264,120 C 355.4066985645933,149.20574162679426 451.92344497607655,162.2200956937799 567,148 C 682.0765550239234,133.7799043062201 815.712918660287,92.32535885167464 902,103 C 988.287081339713,113.67464114832536 1027.2248803827752,176.47846889952154 1109,168 C 1190.7751196172248,159.52153110047846 1315.3875598086124,79.76076555023923 1440,0 L 1440,600 L 0,600 Z");
            }
            50%{
              d: path("M 0,600 L 0,0 C 110.24880382775117,60.794258373205736 220.49760765550235,121.58851674641147 317,140 C 413.50239234449765,158.41148325358853 496.2583732057417,134.44019138755982 581,110 C 665.7416267942583,85.55980861244018 752.4688995215312,60.65071770334927 844,69 C 935.5311004784688,77.34928229665073 1031.866028708134,118.95693779904308 1132,113 C 1232.133971291866,107.04306220095692 1336.066985645933,53.52153110047846 1440,0 L 1440,600 L 0,600 Z");
            }
            75%{
              d: path("M 0,600 L 0,0 C 88.44976076555025,56.6602870813397 176.8995215311005,113.3205741626794 283,131 C 389.1004784688995,148.6794258373206 512.8516746411483,127.37799043062199 620,125 C 727.1483253588517,122.62200956937801 817.6937799043063,139.16746411483257 913,143 C 1008.3062200956937,146.83253588516743 1108.3732057416266,137.95215311004785 1197,112 C 1285.6267942583734,86.04784688995217 1362.8133971291868,43.023923444976084 1440,0 L 1440,600 L 0,600 Z");
            }
            100%{
              d: path("M 0,600 L 0,0 C 117.87559808612443,32.248803827751196 235.75119617224885,64.49760765550239 317,80 C 398.24880382775115,95.50239234449761 442.87081339712915,94.25837320574163 537,93 C 631.1291866028708,91.74162679425837 774.7655502392345,90.46889952153111 870,110 C 965.2344497607655,129.5311004784689 1012.0669856459331,169.86602870813397 1099,155 C 1185.933014354067,140.13397129186603 1312.9665071770335,70.06698564593302 1440,0 L 1440,600 L 0,600 Z");
            }
          }</style><defs><linearGradient id="gradient" x1="0%" y1="50%" x2="100%" y2="50%"><stop offset="5%" stop-color="#f78da7"></stop><stop offset="95%" stop-color="#8ED1FC"></stop></linearGradient></defs><path d="M 0,600 L 0,0 C 117.87559808612443,32.248803827751196 235.75119617224885,64.49760765550239 317,80 C 398.24880382775115,95.50239234449761 442.87081339712915,94.25837320574163 537,93 C 631.1291866028708,91.74162679425837 774.7655502392345,90.46889952153111 870,110 C 965.2344497607655,129.5311004784689 1012.0669856459331,169.86602870813397 1099,155 C 1185.933014354067,140.13397129186603 1312.9665071770335,70.06698564593302 1440,0 L 1440,600 L 0,600 Z" stroke="none" stroke-width="0" fill="url(#gradient)" fill-opacity="0.4" class="transition-all duration-300 ease-in-out delay-150 path-0"></path><style>
          .path-1{
            animation:pathAnim-1 4s;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
          }
          @keyframes pathAnim-1{
            0%{
              d: path("M 0,600 L 0,0 C 65.11961722488039,131.0334928229665 130.23923444976077,262.066985645933 239,303 C 347.7607655502392,343.933014354067 500.16267942583727,294.7655502392344 601,284 C 701.8373205741627,273.2344497607656 751.11004784689,300.8708133971292 837,318 C 922.88995215311,335.1291866028708 1045.397129186603,341.7511961722488 1152,287 C 1258.602870813397,232.24880382775117 1349.3014354066986,116.12440191387559 1440,0 L 1440,600 L 0,600 Z");
            }
            25%{
              d: path("M 0,600 L 0,0 C 91.94258373205744,114.96650717703349 183.8851674641149,229.93301435406698 287,261 C 390.1148325358851,292.066985645933 504.4019138755981,239.23444976076553 588,239 C 671.5980861244019,238.76555023923447 724.507177033493,291.12918660287085 814,311 C 903.492822966507,330.87081339712915 1029.5693779904307,318.2488038277512 1140,261 C 1250.4306220095693,203.7511961722488 1345.2153110047848,101.8755980861244 1440,0 L 1440,600 L 0,600 Z");
            }
            50%{
              d: path("M 0,600 L 0,0 C 94.69856459330143,127.83732057416267 189.39712918660285,255.67464114832535 286,298 C 382.60287081339715,340.32535885167465 481.11004784689,297.1387559808612 580,275 C 678.88995215311,252.86124401913878 778.1626794258374,251.77033492822972 880,275 C 981.8373205741626,298.2296650717703 1086.2392344497607,345.7799043062201 1180,304 C 1273.7607655502393,262.2200956937799 1356.8803827751196,131.11004784688996 1440,0 L 1440,600 L 0,600 Z");
            }
            75%{
              d: path("M 0,600 L 0,0 C 93.22488038277513,84.28708133971291 186.44976076555025,168.57416267942583 278,211 C 369.55023923444975,253.42583732057417 459.42583732057415,253.99043062200957 563,267 C 666.5741626794259,280.00956937799043 783.8468899521533,305.46411483253587 892,314 C 1000.1531100478467,322.53588516746413 1099.1866028708132,314.1531100478469 1189,259 C 1278.8133971291868,203.84688995215313 1359.4066985645934,101.92344497607657 1440,0 L 1440,600 L 0,600 Z");
            }
            100%{
              d: path("M 0,600 L 0,0 C 65.11961722488039,131.0334928229665 130.23923444976077,262.066985645933 239,303 C 347.7607655502392,343.933014354067 500.16267942583727,294.7655502392344 601,284 C 701.8373205741627,273.2344497607656 751.11004784689,300.8708133971292 837,318 C 922.88995215311,335.1291866028708 1045.397129186603,341.7511961722488 1152,287 C 1258.602870813397,232.24880382775117 1349.3014354066986,116.12440191387559 1440,0 L 1440,600 L 0,600 Z");
            }
          }</style><defs><linearGradient id="gradient" x1="0%" y1="50%" x2="100%" y2="50%"><stop offset="5%" stop-color="#f78da7"></stop><stop offset="95%" stop-color="#8ED1FC"></stop></linearGradient></defs><path d="M 0,600 L 0,0 C 65.11961722488039,131.0334928229665 130.23923444976077,262.066985645933 239,303 C 347.7607655502392,343.933014354067 500.16267942583727,294.7655502392344 601,284 C 701.8373205741627,273.2344497607656 751.11004784689,300.8708133971292 837,318 C 922.88995215311,335.1291866028708 1045.397129186603,341.7511961722488 1152,287 C 1258.602870813397,232.24880382775117 1349.3014354066986,116.12440191387559 1440,0 L 1440,600 L 0,600 Z" stroke="none" stroke-width="0" fill="url(#gradient)" fill-opacity="0.53" class="transition-all duration-300 ease-in-out delay-150 path-1"></path><style>
          .path-2{
            animation:pathAnim-2 4s;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
          }
          @keyframes pathAnim-2{
            0%{
              d: path("M 0,600 L 0,0 C 77.24401913875596,152.14354066985646 154.48803827751192,304.2870813397129 269,370 C 383.5119617224881,435.7129186602871 535.2918660287081,414.9952153110048 627,397 C 718.7081339712919,379.0047846889952 750.3444976076554,363.73205741626793 835,393 C 919.6555023923446,422.26794258373207 1057.33014354067,496.07655502392345 1167,438 C 1276.66985645933,379.92344497607655 1358.334928229665,189.96172248803828 1440,0 L 1440,600 L 0,600 Z");
            }
            25%{
              d: path("M 0,600 L 0,0 C 119.91387559808612,184.87081339712918 239.82775119617224,369.74162679425837 326,435 C 412.17224880382776,500.25837320574163 464.6028708133972,445.9043062200957 553,408 C 641.3971291866028,370.0956937799043 765.7607655502393,348.64114832535887 872,371 C 978.2392344497607,393.35885167464113 1066.3540669856459,459.5311004784689 1158,405 C 1249.6459330143541,350.4688995215311 1344.8229665071772,175.23444976076556 1440,0 L 1440,600 L 0,600 Z");
            }
            50%{
              d: path("M 0,600 L 0,0 C 124.64114832535887,167.95215311004785 249.28229665071774,335.9043062200957 326,406 C 402.71770334928226,476.0956937799043 431.51196172248797,448.3349282296651 523,437 C 614.488038277512,425.6650717703349 768.6698564593302,430.755980861244 894,433 C 1019.3301435406698,435.244019138756 1115.8086124401914,434.64114832535887 1202,362 C 1288.1913875598086,289.35885167464113 1364.0956937799042,144.67942583732057 1440,0 L 1440,600 L 0,600 Z");
            }
            75%{
              d: path("M 0,600 L 0,0 C 98.82296650717703,148.36363636363635 197.64593301435406,296.7272727272727 295,367 C 392.35406698564594,437.2727272727273 488.2392344497607,429.4545454545454 595,431 C 701.7607655502393,432.5454545454546 819.3971291866029,443.45454545454544 906,460 C 992.6028708133971,476.54545454545456 1048.1722488038279,498.7272727272727 1132,423 C 1215.8277511961721,347.2727272727273 1327.9138755980862,173.63636363636365 1440,0 L 1440,600 L 0,600 Z");
            }
            100%{
              d: path("M 0,600 L 0,0 C 77.24401913875596,152.14354066985646 154.48803827751192,304.2870813397129 269,370 C 383.5119617224881,435.7129186602871 535.2918660287081,414.9952153110048 627,397 C 718.7081339712919,379.0047846889952 750.3444976076554,363.73205741626793 835,393 C 919.6555023923446,422.26794258373207 1057.33014354067,496.07655502392345 1167,438 C 1276.66985645933,379.92344497607655 1358.334928229665,189.96172248803828 1440,0 L 1440,600 L 0,600 Z");
            }
          }</style><defs><linearGradient id="gradient" x1="0%" y1="50%" x2="100%" y2="50%"><stop offset="5%" stop-color="#f78da7"></stop><stop offset="95%" stop-color="#8ED1FC"></stop></linearGradient></defs><path d="M 0,600 L 0,0 C 77.24401913875596,152.14354066985646 154.48803827751192,304.2870813397129 269,370 C 383.5119617224881,435.7129186602871 535.2918660287081,414.9952153110048 627,397 C 718.7081339712919,379.0047846889952 750.3444976076554,363.73205741626793 835,393 C 919.6555023923446,422.26794258373207 1057.33014354067,496.07655502392345 1167,438 C 1276.66985645933,379.92344497607655 1358.334928229665,189.96172248803828 1440,0 L 1440,600 L 0,600 Z" stroke="none" stroke-width="0" fill="url(#gradient)" fill-opacity="1" class="transition-all duration-300 ease-in-out delay-150 path-2"></path></svg>
