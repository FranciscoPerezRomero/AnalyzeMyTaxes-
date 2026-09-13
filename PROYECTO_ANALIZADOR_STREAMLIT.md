# Proyecto: Analizador de Finanzas Personales

## Contexto para Claude

Cisco es desarrollador Fullstack Jr. practicando Python con Pandas — la habilidad central de este
proyecto — y Plotly para las visualizaciones interactivas.
Este proyecto usa Streamlit como interfaz web — es su primera vez con esta librería.
El objetivo es aprender manejo de datos mientras construye algo presentable para su portafolio.

**Reglas para Claude en estas sesiones:**
- No escribir el código completo — guiar con preguntas y pistas
- Explicar el *por qué* de cada decisión técnica
- Si Cisco se atasca más de 10 minutos, dar una pista, no la solución
- Al final de cada módulo preguntar: ¿puedes explicar qué hace cada parte?

---

## Descripción del proyecto

Herramienta web construida con Streamlit que permite cargar el registro de movimientos financieros
personales del usuario (CSV o Excel `.xlsx` — un extracto bancario exportado, una planilla propia de
gastos, lo que ya tenga) y automáticamente genera resumen de ingresos/gastos, distribución por
categoría, evolución en el tiempo y balance. El usuario no necesita saber programación, Excel ni
ningún formato específico — solo sube lo que ya tiene.

**Qué NO hace este proyecto (fuera de alcance, a propósito):**
- No calcula impuestos — depende de jurisdicción/régimen fiscal, es un dominio legal/contable
  aparte, no algo que resuelva un análisis de datos genérico.
- No hace proyecciones ni forecasting — el foco es análisis descriptivo de lo ya ocurrido.
- No asesora financieramente ni da recomendaciones — solo muestra los datos que el usuario ya tiene.

**Mapeo de columnas (decisión de diseño clave):**
Como cada banco/persona exporta sus movimientos con nombres de columna distintos ("Fecha" vs
"Date" vs "Fecha transacción"), la app NO asume nombres fijos. Después de subir el archivo, el
usuario indica con selectores (`st.selectbox`) cuáles de sus columnas corresponden a:
- **Fecha** de la transacción
- **Monto** (positivo/negativo, o con una columna de tipo aparte)
- **Categoría** (opcional — si no existe, se omiten las vistas que dependen de categoría)
- **Descripción** (opcional)

Esto mantiene el "funciona con cualquier archivo" sin tener que adivinar la estructura, y es el
mismo patrón de selector que ya vas a usar en el Módulo 5 (filtros) — así que sirve como
introducción temprana a `st.selectbox()`.

Si el archivo es Excel y tiene varias hojas, el usuario elige cuál analizar (una tabla a la vez,
sin combinar hojas automáticamente — eso mantiene el alcance simple).

**Stack:**
- Python
- Pandas — manipulación y análisis de datos (incluye `read_csv` y `read_excel`) — la herramienta
  central que se está practicando en este proyecto
- openpyxl — motor para que Pandas pueda leer archivos `.xlsx`
- Plotly (Plotly Express) — visualizaciones interactivas (hover, zoom), en vez de Matplotlib/Seaborn
  — decisión consciente: se prioriza interactividad para el dashboard, ya que Pandas es la
  habilidad que más transfiere a otros contextos, y la librería de gráficas es más intercambiable
- Streamlit — interfaz web

**Deploy:** Streamlit Community Cloud (gratis, URL pública para portafolio)

---

## Módulos del proyecto

### Módulo 1 — Setup, carga y mapeo de columnas
**Objetivo:** Tener Streamlit corriendo, con el usuario pudiendo subir su archivo y decirle a la
app qué columna es cuál.

Tareas:
- Instalar dependencias: `pip install streamlit pandas plotly openpyxl`
- Crear estructura de carpetas del proyecto
- Página principal con título, descripción y uploader (acepta `.csv` y `.xlsx`)
- Detectar la extensión del archivo y leer con `read_csv` o `read_excel` según corresponda
- Si es Excel con varias hojas, selector de hoja
- Mostrar el DataFrame crudo
- Selectores para que el usuario mapee sus columnas a: Fecha, Monto, Categoría (opcional),
  Descripción (opcional)

Criterio de éxito: al correr `streamlit run app.py`, subir un archivo propio (CSV o Excel) y
mapear sus columnas, la app reconoce cuáles son fecha/monto/categoría sin importar cómo se llamen
originalmente.

---

### Módulo 2 — Resumen financiero
**Objetivo:** Mostrar un resumen de ingresos, gastos y balance a partir de la columna de Monto.

Tareas:
- Total de ingresos (montos positivos) y total de gastos (montos negativos, en valor absoluto)
- Balance neto (ingresos − gastos)
- Número de transacciones y rango de fechas cubierto
- Gasto promedio por transacción
- Valores nulos por columna (para que el usuario sepa si su archivo tiene datos incompletos)
- Mostrar todo con `st.metric()`, `st.dataframe()` y `st.write()`

Criterio de éxito: al subir un archivo y mapear columnas, aparece un resumen claro de cuánto
entró, cuánto salió y el balance.

---

### Módulo 3 — Visualizaciones automáticas
**Objetivo:** Mostrar gráficas sobre cómo se distribuye el dinero.

Tareas:
- Gráfica de barras: gasto total por categoría (si el usuario mapeó una columna de categoría) —
  `px.bar()`
- Línea de tiempo: evolución del balance o del gasto acumulado según la columna de Fecha —
  `px.line()`
- Histograma de la distribución de montos — `px.histogram()`
- Mostrar cada gráfica con `st.plotly_chart(fig)` (no `st.pyplot()`, que es para Matplotlib)

Criterio de éxito: el usuario ve en qué categorías gasta más y cómo evoluciona su dinero en el
tiempo.

---

### Módulo 4 — Relaciones entre variables
**Objetivo:** Mostrar relaciones entre las columnas numéricas disponibles (más allá de Monto, si
el archivo trae otras — ej. cantidad de ítems, cuotas).

Tareas:
- Matriz de correlación con `df.corr()` sobre las columnas numéricas del archivo
- Heatmap con `px.imshow()` (equivalente en Plotly al heatmap de Seaborn, pero interactivo)
- Scatter plot entre dos columnas numéricas seleccionadas por el usuario — `px.scatter()`
- Si el archivo solo tiene una columna numérica (Monto), mostrar un mensaje claro de que no hay
  suficientes variables para correlacionar, en vez de romper

Criterio de éxito: cuando el archivo lo permite, el usuario puede explorar relaciones entre pares
de variables numéricas.

---

### Módulo 5 — Filtros interactivos
**Objetivo:** Permitir filtrar los movimientos y ver cómo cambian el resumen y las gráficas.

Tareas:
- Selector de rango de fechas (filtra por la columna de Fecha mapeada)
- Multiselect para filtrar por categoría (si existe)
- Slider para filtrar por rango de monto
- Actualizar resumen financiero y gráficas en tiempo real
- Mostrar cuántas transacciones quedan después del filtro

Criterio de éxito: los filtros actualizan todo el dashboard automáticamente.

---

### Módulo 6 — Exportar resultados
**Objetivo:** Permitir descargar los movimientos filtrados y el resumen financiero.

Tareas:
- Botón para descargar CSV filtrado con `st.download_button()`
- Botón para descargar el resumen financiero como CSV
- Mensaje de confirmación al descargar

Criterio de éxito: el usuario puede descargar los resultados de su análisis.

---

### Módulo 7 — Pulir y deployar
**Objetivo:** Dejar el proyecto presentable y publicado con URL pública.

Tareas:
- Manejo de errores: archivo vacío, sin columna reconocible como monto/fecha, mapeo incompleto,
  archivo inválido
- Mejorar textos y mensajes al usuario (aclarar que no calcula impuestos ni da asesoría)
- Agregar README con descripción del proyecto
- Crear cuenta en Streamlit Community Cloud
- Conectar repositorio de GitHub y deployar
- Verificar que funciona con la URL pública

Criterio de éxito: cualquier persona puede abrir la URL, subir su propio archivo de movimientos y
usar la herramienta sin instrucciones adicionales.

---

## Estado del proyecto

- [ ] Módulo 1 — Setup, carga y mapeo de columnas
- [ ] Módulo 2 — Resumen financiero
- [ ] Módulo 3 — Visualizaciones automáticas
- [ ] Módulo 4 — Relaciones entre variables
- [ ] Módulo 5 — Filtros interactivos
- [ ] Módulo 6 — Exportar resultados
- [ ] Módulo 7 — Pulir y deployar

---

## Notas

- Usar datasets públicos de Kaggle o extractos bancarios de ejemplo (anonimizados) para probar
  durante el desarrollo
- El proyecto debe funcionar con CUALQUIER archivo de movimientos (CSV o Excel), sin asumir
  nombres de columna fijos — de ahí el mapeo de columnas del Módulo 1
- Priorizar que funcione bien antes de que se vea bien
