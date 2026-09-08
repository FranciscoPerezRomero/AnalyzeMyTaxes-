# Proyecto: Analizador de Datos Personal

## Contexto para Claude

Cisco es desarrollador Fullstack Jr. practicando Python con Pandas y Matplotlib.
Este proyecto usa Streamlit como interfaz web — es su primera vez con esta librería.
El objetivo es aprender manejo de datos mientras construye algo presentable para su portafolio.

**Reglas para Claude en estas sesiones:**
- No escribir el código completo — guiar con preguntas y pistas
- Explicar el *por qué* de cada decisión técnica
- Si Cisco se atasca más de 10 minutos, dar una pista, no la solución
- Al final de cada módulo preguntar: ¿puedes explicar qué hace cada parte?

---

## Descripción del proyecto

Herramienta web construida con Streamlit que permite cargar cualquier archivo CSV
y automáticamente genera estadísticas descriptivas y visualizaciones interactivas.
El usuario no necesita saber programación — solo sube su archivo y explora los datos.

**Stack:**
- Python
- Pandas — manipulación y análisis de datos
- Matplotlib / Seaborn — visualizaciones
- Streamlit — interfaz web

**Deploy:** Streamlit Community Cloud (gratis, URL pública para portafolio)

---

## Módulos del proyecto

### Módulo 1 — Setup y estructura base
**Objetivo:** Tener Streamlit corriendo con una interfaz básica.

Tareas:
- Instalar dependencias: `pip install streamlit pandas matplotlib seaborn`
- Crear estructura de carpetas del proyecto
- Página principal con título, descripción y uploader de archivos
- Mostrar el DataFrame crudo cuando se sube un archivo

Criterio de éxito: al correr `streamlit run app.py` aparece una página con uploader funcional.

---

### Módulo 2 — Resumen estadístico
**Objetivo:** Mostrar estadísticas descriptivas del dataset cargado.

Tareas:
- Número de filas y columnas
- Tipos de datos por columna
- Valores nulos por columna
- Estadísticas descriptivas con `df.describe()`
- Mostrar todo con `st.metric()`, `st.dataframe()` y `st.write()`

Criterio de éxito: al subir un CSV aparece un resumen claro del contenido.

---

### Módulo 3 — Visualizaciones automáticas
**Objetivo:** Generar gráficas útiles según el tipo de dato de cada columna.

Tareas:
- Detectar columnas numéricas vs categóricas
- Histograma para columnas numéricas
- Gráfica de barras para columnas categóricas
- Selector de columna con `st.selectbox()`
- Mostrar gráfica con `st.pyplot()`

Criterio de éxito: el usuario puede elegir cualquier columna y ver su distribución.

---

### Módulo 4 — Análisis de correlaciones
**Objetivo:** Mostrar relaciones entre variables numéricas.

Tareas:
- Matriz de correlación con `df.corr()`
- Heatmap con Seaborn
- Scatter plot entre dos columnas seleccionadas por el usuario
- Dos selectores: columna X y columna Y

Criterio de éxito: el usuario puede explorar relaciones entre cualquier par de variables.

---

### Módulo 5 — Filtros interactivos
**Objetivo:** Permitir al usuario filtrar los datos y ver cómo cambian las estadísticas.

Tareas:
- Slider para filtrar columnas numéricas por rango
- Multiselect para filtrar columnas categóricas por valor
- Actualizar todas las estadísticas y gráficas en tiempo real
- Mostrar cuántos registros quedan después del filtro

Criterio de éxito: los filtros actualizan todo el dashboard automáticamente.

---

### Módulo 6 — Exportar resultados
**Objetivo:** Permitir descargar el dataset filtrado y las estadísticas.

Tareas:
- Botón para descargar CSV filtrado con `st.download_button()`
- Botón para descargar resumen estadístico como CSV
- Mensaje de confirmación al descargar

Criterio de éxito: el usuario puede descargar los resultados de su análisis.

---

### Módulo 7 — Pulir y deployar
**Objetivo:** Dejar el proyecto presentable y publicado con URL pública.

Tareas:
- Agregar manejo de errores: CSV vacío, columnas sin datos, archivo inválido
- Mejorar textos y mensajes al usuario
- Agregar README con descripción del proyecto
- Crear cuenta en Streamlit Community Cloud
- Conectar repositorio de GitHub y deployar
- Verificar que funciona con la URL pública

Criterio de éxito: cualquier persona puede abrir la URL y usar la herramienta.

---

## Estado del proyecto

- [ ] Módulo 1 — Setup y estructura base
- [ ] Módulo 2 — Resumen estadístico
- [ ] Módulo 3 — Visualizaciones automáticas
- [ ] Módulo 4 — Análisis de correlaciones
- [ ] Módulo 5 — Filtros interactivos
- [ ] Módulo 6 — Exportar resultados
- [ ] Módulo 7 — Pulir y deployar

---

## Notas

- Usar datasets públicos de Kaggle para probar durante el desarrollo
- El proyecto debe funcionar con CUALQUIER CSV, no solo uno específico
- Priorizar que funcione bien antes de que se vea bien
