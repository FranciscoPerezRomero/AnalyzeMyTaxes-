import streamlit as st
import modules.load_fileModule as load
import modules.data_analystModule as dt
import modules.graphicsModule as gp

st.set_page_config(layout="wide")

st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #1e1e2f;
    border-radius: 12px;
    padding: 16px 20px;
    max-width: 225px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
[data-testid="stMetricLabel"] {
    font-size: 0.85rem;
    opacity: 0.7;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
[data-testid="stMetricValue"] {
    font-size: 2rem;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

def main():
    data = load.load_file()
    if data is not None:
        # * Mapeo de columnas: el usuario indica cuáles de sus columnas
        # * corresponden a Monto, Fecha y Categoría, sin asumir nombres fijos
        st.subheader("Mapeo de columnas")
        map1, map2, map3 = st.columns(3)
        with map1:
            column = st.selectbox("¿Cuál es tu columna de Monto?", options=data.select_dtypes(include='number').columns)
        with map2:
            fecha_col = st.selectbox("¿Cuál es tu columna de Fecha?", options=data.columns)
        with map3:
            categoria_col = st.selectbox("¿Cuál es tu columna de Categoría?", options=data.columns)

        dt.dataAnalyst(data, column)
        gp.graphics_analyst(data, column, fecha_col, categoria_col)

if __name__ == '__main__':
    main()