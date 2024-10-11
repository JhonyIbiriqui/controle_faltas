import streamlit as st
import pandas as pd


#st.set_page_config(layout="wide")
tb_base = pd.read_csv("datasets/Controle de faltas.csv")


#tb_base["DATA"] = pd.to_datetime(tb_base["DATA"], dayfirst=True, errors='coerce')

substituicoes = {
    "JHONY": "JHONY ALLISON",
    "HUGO": "HUGO MANICARDI",
    "RAFAELA": "RAFAELA LUPPI"
}

tb_base["NOME COLABORADOR"] = tb_base["NOME COLABORADOR"].replace(substituicoes)

logo = "assets/LOGO_MARIMEL.png"

with st.container():
    title = st.title("Controle de Faltas - :red[RH]")
    st.divider()


#datamax = tb_base["DATA"].max()
#datamin = tb_base["DATA"].min()


with st.sidebar:
    st.logo(logo,size="large" )
    Colab_select_box = st.selectbox("Colaboradores", tb_base["NOME COLABORADOR"].unique())
    

#Filtra_data = st.sidebar.slider("Data da Falta: ", datamin, datamax, datamax)

df_select_box_filtrado = tb_base[tb_base["NOME COLABORADOR"] == Colab_select_box]

KPI_faltas = df_select_box_filtrado.groupby("TIPO")["TEMPO(DIAS)"].sum().reset_index()

title= st.title(f"Total de Faltas para {Colab_select_box}")

num_kpis = len(KPI_faltas)
col = st.columns(num_kpis)

for index, row in KPI_faltas.iterrows():
    col[index].metric(label=row["TIPO"], value=row["TEMPO(DIAS)"])

st.subheader("Dados Filtrados: ")

df_filtrado_ordenado = df_select_box_filtrado.sort_values(by="DATA", ascending=False)

df_filtrado_ordenado


        