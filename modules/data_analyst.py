import pandas as pd
import streamlit as st
import plotly.express as px

def dataAnalyst(data):
    df = data
    namesColumns = df.select_dtypes(include='number').columns
    # * Selección de columna de datos
    column = st.selectbox("Elige la columna con tus gastos", options=namesColumns)

    # * DataFrame de datos positivos
    numDataPositive = df[(df[column]) > 0 ]
    # * DataFrame de datos Negativos
    numDataNegative = df[(df[column]) < 0 ]

    # * Calculo de totales
    ingresos = numDataPositive[column].sum()
    gastos = numDataNegative[column].sum()

    # *Calculo de gasto medio
    gasto_medio = abs(numDataNegative[column]).mean()

    # ? Se define como mostrar información
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gastos del mes")
        st.write(numDataPositive)
    with col2:
        st.subheader("Gastos del mes")
        st.write(numDataNegative)
   
    # ? Columnas de metricas
    totales, estadistica = st.columns (2)
    with totales:
        st.subheader("")
        st.metric("Ingresos", ingresos)
        st.metric("Gastos", gastos)
        st.metric("Balance", ingresos - abs(gastos))
    with estadistica:
        # * Impresión de media de la columna
        st.metric("Gasto medio", abs(gasto_medio))

    return column
    
