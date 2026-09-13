import pandas as pd
import streamlit as st
import plotly.express as px

def graphics_analyst(data, column):
    # * Filtrado de gastos separado en serie
    gasto = data[(data[column] < 0)]
    # * Reemplazo de montos negativo a positivo
    gasto[column] = gasto[column].abs()
    # * Agrupación por categoría y grafico
    st.subheader("Distribución de gastos")
    st.write(px.bar(gasto.groupby("Categoria")["Monto"].sum().reset_index(), x="Categoria", y="Monto"))

