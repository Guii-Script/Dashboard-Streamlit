import streamlit as st
import pandas as pd

# Título do App
st.title("Meu Primeiro Dashboard")
st.write("Olá, mundo!")

# Criando um conjunto de dados de exemplo com Pandas
dados = pd.DataFrame({
  'Vendas': [10, 20, 35, 30, 5],
  'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai']
})

# Adicionando elementos do dashboard
st.header("Gráfico de Vendas Mensais")

st.write("Aqui estão os dados:")
st.dataframe(dados) # Mostra a tabela de dados interativa

st.write("E aqui está o gráfico:")
st.bar_chart(data=dados, x='Mês', y='Vendas') # Cria o gráfico de barras