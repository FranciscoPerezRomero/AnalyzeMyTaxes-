import streamlit as st
import padnas as pd
def main():
    st.title("Hola mundo")
    st.header("Esto es un titulo")
    st.subheader("Esto es un subtitulo")
    st.text("Esto es un texto")
    nombre = 'francisco'
    st.text(f'Identando texto mi nombre {nombre}')
    st.markdown("###Usando markdown para la página")
    st.success("Confirmado")

if __name__ == '__main__':
    main()