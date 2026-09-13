import streamlit as st
import modules.load_fileModule as load
import modules.data_analyst as dt
import modules.graphics as gp

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
        column = dt.dataAnalyst(data)
        gp.graphics_analyst(data, column)

if __name__ == '__main__':
    main()