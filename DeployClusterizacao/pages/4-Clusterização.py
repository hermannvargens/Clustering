
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv('data.csv')
var_cat=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
var_num=['tenure', 'MonthlyCharges', 'TotalCharges']


########################CLUSTERS######################

st.subheader("Principais características de cada cluster")

st.write("Distribuição dos cluster")
option_num_X = st.selectbox(
    'Selecione uma variável para o eixo X:',
    (var_num))
option_num_Y = st.selectbox(
    'Selecione uma variável para o eixo Y:',
    (var_num))
st.plotly_chart(px.scatter(data, x=option_num_X, y=option_num_Y, color="Cluster"))

st.write("Relação de cada cluster com as variáveis numéricas")
option_num = st.selectbox(
    'Selecione uma variável:',
    (var_num))
st.plotly_chart(px.box(data, x="Cluster", y= option_num, color=None))

st.write("Podemos concluir que: \n \
         \n - **Cluster 0**: possui o tempo de permanência com a empresa médio, e os menores valores de cobrança mensal e menores valores de cobrança, ao longo da vida como cliente.\
        \n - **Cluster 1**: possui o maior tempo de permanência com a empresa e os maiores valores de cobrança mensal e, portanto, são os **clientes que mais trazem receita para a empresa**.\
        \n - **Cluster 2**: possui, em média, o menor tempo de permanência com a empresa (menor tenure), mas possui altos valores de cobrança mensal.")