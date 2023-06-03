import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
##########ANÁLISE EXPLORATÓRIA COM VISUALIZAÇÃO##########

import plotly.express as px
import plotly.graph_objects as go



data = pd.read_csv('data.csv')
var_cat=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
var_num=['tenure', 'MonthlyCharges', 'TotalCharges']

st.header('Análise Exploratória de Dados com Visualização Gráfica')


#st.write('**Variáveis numéricas**')
#PIE CHART
st.write('***Variável target: Churn rate***')
labels = ['No','Yes']
values = data['Churn'].value_counts()

st.plotly_chart(go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0.1, 0])]))


# BAR CHART # BOXPLOT

st.write('***Variáveis numéricas***')

option = st.selectbox(
    'Selecione uma das variáveis abaixo:',
    (var_num))


tab_distribuicao, tab_boxplot = st.tabs(["Distribuição", "Boxplot"])

with tab_distribuicao:

    st.plotly_chart(px.histogram(data, option))

with tab_boxplot:

    mostrar_churn = st.checkbox("Mostrar gráfico com Churn")

    if mostrar_churn:
        st.plotly_chart(px.box(data, y=option, color="Churn"))
    else:
        st.plotly_chart(px.box(data, y=option))


# BAR PLOT

st.write('***Variáveis categóricas***')

option_cat = st.selectbox(
    'Selecione uma das variáveis abaixo:',
    (var_cat))

if option_cat == "gender":
    st.write('O dataset possui aproximadamente a mesma quantidade de homens e mulheres')
if option_cat == "SeniorCitizen":
    st.write('***Há muito menos idosos, no entanto, grande parte deles irá deixar a empresa em algum momento.')
if option_cat == "Partner":
    st.write('Proporcionalmente, clientes que não têm parceiros churnam mais que clientes que têm parceiros.')
if option_cat == "Dependents":
    st.write('A quantidade de clientes que não possuem dependentes é pouco mais que a metade dos clientes que possuem, no entanto, a probabilidade destes últimos abandorarema a empresa é menor')
if option_cat == "PhoneService":
    st.write('A maioria dos clientes posssuem serviços de telefone.')
if option_cat == "MultipleLines":
    st.write('Possuir múltiplas linhas não muda consideravalmente a probabilidade de churnar')
if option_cat == "InternetService":
    st.write('***Clientes que possuem Fiber optic (fibra óptica) churnam com mais facilidade.')
if option_cat == "OnlineSecurity":
    st.write('Clientes que não possuem OnlineSecurity churnam mais do que clientes que possuem.')
if option_cat == "OnlineBackup":
    st.write('Clientes que possuem OnlineBackup churnam menos do que clientes que não possuem.')
if option_cat == "DeviceProtection":
    st.write('Clientes que não possuem DeviceProtection churnam mais.')
if option_cat == "TechSupport":
    st.write('Clientes que não possuem e TechSupport churnam mais.')
if option_cat == "StreamingTV":
    st.write('Possuir StreamingTV não é um fator relevante para o cliente decidir churnar. ')
if option_cat == "StreamingMovies":
    st.write('Possuir StreamingMovies não é um fator relevante para o cliente decidir churnar. ')
if option_cat == "Contract":
    st.write('***Quanto maior o prazo do contrato, menos os clientes churnam.')
if option_cat == "PaperlessBilling":
    st.write('***Clientes que recebem fatura em meios que não utilizam papel churnam mais que clientes que recebem.')
if option_cat == "PaymentMethod":
    st.write('***Clientes que utilizam meios eletrônicos para pagamentos churnam mais que clientes que utilizam outros meios.')

st.plotly_chart(px.histogram(data, x=option_cat, color="Churn", barmode='group'))