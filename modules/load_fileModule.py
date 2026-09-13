import streamlit as st
import pandas as pd
import openpyxl as pyxl
def load_file():
    #* Extensiones de archivos soportadas
    extensions = ['csv','xlsx']
    # * Lectura de archivos 
    st.title("Analisis de cuentas personales")
    upload_file = st.file_uploader("Elige el archivo que quieras analizar", type=extensions)
    # * Dibujar tabla solo en caso de que ya se haya cargado información
    if upload_file is not None:
        if upload_file.name.endswith('.xlsx'):
            # * Se obtienen los nombres de las hojas de excel
            sheet_names = pd.ExcelFile(upload_file).sheet_names
            selected = st.selectbox('Elige una hoja para analizar', options=sheet_names)
            data = pd.read_excel(upload_file, sheet_name=selected)
            # * Mostrar datos
            st.title('\nDatos cargados')
            st.write(data)
            return data
        elif upload_file.name.endswith('csv'):
            data = pd.read_csv(upload_file)
            # * Mostrar datos
            st.title("\nVisualizar datos")
            st.write(data)
            return data