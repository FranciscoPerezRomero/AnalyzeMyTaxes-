import pandas as pd
import streamlit as st

def dataAnalyst(data):
    df = pd.DataFrame(data)
    namesColumns = df.select_dtypes(include='number').columns
    # * Selección de columna de datos
    column = st.selectbox("Elige la columna con tus gastos", options=namesColumns)
    # * DataFrame de datos positivos
    numDataPositive = df[(df[column]) > 0 ]
    # * DataFrame de datos Negativos
    numDataNegative = df[(df[column]) < 0 ]

    # ? Se define como mostrar información
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Gastos del mes")
        st.write(numDataPositive)
    with col2:
        st.subheader("Gastos del mes")
        st.write(numDataNegative)
    
