import streamlit as st
import modules.load_fileModule as load
import modules.data_analyst as dt

st.set_page_config(layout="wide")

def main():
    data = load.load_file()
    if data is not None:
        dt.dataAnalyst(data)

if __name__ == '__main__':
    main()