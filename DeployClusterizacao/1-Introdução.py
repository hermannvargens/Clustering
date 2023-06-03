import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

st.header("Entendendo os clientes de uma empresa de Telecomunicações através de Clusterização")

st.write("Este projeto tem como objetivo analisar base de dados de uma empresa de telefonia, que contém informações dos seus clientes, entre elas \
         se o cliente deixou a empresa (*churn*) e quanto tempo cada um deles permaneceu com a empresa antes de deixá-la,\
         de modo a entender como as características mais relevantes se relacionam com as receitas obtidas pela empresa, e também com o *churn rate*. \n")

st.write("Responderemos tammbém algumas perguntas de negócio através de consulta ao banco de dados, para obter outros *insights* relevantes. \n")

st.write("Finalmente, aplicaremos o algoritmo de clusterização *K-Prototypes* para segmentar os clientes em diferentes grupos e entender melhor como cada grupo contribui com as receitas \
         e o *churn rate* da empresa.")


data = pd.read_csv('data.csv')

var_cat=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
var_num=['tenure', 'MonthlyCharges', 'TotalCharges']

mostrar_dados = st.checkbox("Mostrar dados")
if mostrar_dados:
    st.write(data.drop(columns="Cluster"))
         

