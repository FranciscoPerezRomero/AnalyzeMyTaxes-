import pandas as pd
import streamlit as st
import plotly.express as px

def graphics_analyst(data, column, fecha_col, categoria_col):
    # * Filtrado de gastos separado en serie
    gasto = data[(data[column] < 0)].copy()
    # * Orden de dataset (sort_values no ordena "en el lugar", hay que reasignar)
    gasto = gasto.sort_values(by=fecha_col)
    # * Reemplazo de montos negativo a positivo
    gasto[column] = gasto[column].abs()
    # * Calculo de gasto acumulado timeline
    gasto["Acumulado"] = gasto[column].cumsum()
    # * Agrupación por categoría y grafico
    st.subheader("Distribución de gastos")
    st.write(px.bar(gasto.groupby(categoria_col)[column].sum().reset_index(), x=categoria_col, y=column))
    # * Linea del tiempo
    st.subheader("Linea de gastos acumulados")
    st.write(px.line(gasto, x=fecha_col, y="Acumulado", markers=True))
    # * Histograma
    st.subheader("Histograma de movimientos")
    st.write(px.histogram(gasto, x=column))

