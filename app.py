import streamlit as st
import pandas as pd

st.set_page_config(page_title="Monitor de Preços", layout="wide")
st.title("Monitor de Preços - Kabum")

# Corrigido: FileNotFoundError, não FileExistsError
try:
    df = pd.read_csv("precos.csv", names=["Data", "Produto", "Preço"], parse_dates=["Data"])
except FileNotFoundError:
    st.warning("Arquivo de histórico ainda não existe.")
    st.stop()

# Interface
produto_selecionado = st.selectbox("Escolha um produto", df["Produto"].unique())

# Filtro e visualização
df_filtrado = df[df["Produto"] == produto_selecionado]

# Gráfico
st.line_chart(df_filtrado.set_index("Data")["Preço"])

# Tabela
st.dataframe(df_filtrado.sort_values("Data", ascending=False), use_container_width=True)
