import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

#st.set_page_config(layout="wide")
tb_base = pd.read_csv('datasets/Controle de faltas.csv')
tb_base["DATA"] = pd.to_datetime(tb_base["DATA"], dayfirst=True, errors='coerce')

tb_base_new = tb_base.sort_values(by="DATA", ascending=False)





logo = "assets/LOGO_MARIMEL.png"

with st.container():
    title = st.title("Controle de Faltas - :red[RH]")
    st.divider()

with st.sidebar:
    st.logo(logo,size="large" )
   
    #Colab_select_box = st.selectbox("Colaboradores", tb_base["NOME COLABORADOR"].unique())
    



tb_base_new