import streamlit as st
import pandas as pd
import numpy as np


st.header("Perguntas de Negócio") 


data = pd.read_csv('data.csv')


#####
var_cat=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']
var_num=['tenure', 'MonthlyCharges', 'TotalCharges']



#PERGUNTA 1
st.write('**P1 - Qual o *churn rate* da empresa, isto é, qual a porcentagem de clientes que deixou o serviço?**')

st.write(data['Churn'].value_counts())
st.write((f'O churn rate da empresa é de {1869/(1869+5174):.2%}.'))

#PERGUNTA 2
st.write('**P2 - Por quanto tempo em média, os clientes permanecem ativos antes de deixar a empresa?**')

media_tenure = data[data['Churn'] == 'Yes']['tenure'].mean()
mediana_tenure = data[data['Churn'] == 'Yes']['tenure'].median()
st.write(pd.DataFrame({'media':[media_tenure],'mediana':[mediana_tenure]}))

st.write(f'A média de meses que o cliente leva para deixar a empresa é de {media_tenure:.2f} meses.\n\
A mediana corresponde a {mediana_tenure} meses.')

#PERGUNTA 3
st.write('**P3 - Qual a porcetagem de clientes que deixa a empresa nos primeiros 10 meses?**')

churn_10meses = data[(data['tenure']<=10) & (data['Churn']=='Yes')].shape[0]
st.write(pd.DataFrame({'churn_10meses':[churn_10meses],'churn_10meses_porcento':[churn_10meses/data.shape[0]*100]}))

st.write(f'Nos 10 primeiros meses, {churn_10meses/data.shape[0] :.2%} dos clientes totais irão churnar.')

#PERGUNTA 4
st.write("**P4 - Qual o valor de receita mensal arrecadada das pessoas que churnam? Ela corresponde a quantos porcento da receita mensal total?**")

receita_mensal_churn = data[data['Churn'] == 'Yes']['MonthlyCharges'].sum()
receita_mensal_total = data['MonthlyCharges'].sum()
st.write(pd.DataFrame({'receita_mensal_churn':[receita_mensal_churn],'receita_mensal_total':[receita_mensal_total],'porcentagem_receita':[receita_mensal_churn/receita_mensal_total*100]}))

st.write(f'O valor mensalmente arrecadado proveniente das pessoas que churnam é $ {receita_mensal_churn:,.2f}. \
Este valor corresponde a {receita_mensal_churn/receita_mensal_total:.2%} da receita mensal total.')

#PERGUNTA 5
st.write('**P5 - Se fizéssemos uma campanha de marketing para aumentar o tempo de permanência com a empresa (tenure) em 12 meses, com 100% de adesão dos clientes que churnam, qual seria o impacto dessa campanha na receita total dos clientes?**')

data['nova_tenure']=data['tenure'] + 12
data['novo_TotalCharges'] = data['nova_tenure']*data['MonthlyCharges']
data[['tenure','nova_tenure','MonthlyCharges','TotalCharges','novo_TotalCharges','Churn']].head(5)

receita_total = data['TotalCharges'].sum()

receita_total_nova = data['novo_TotalCharges'].sum()
dif_percentual = (receita_total_nova - receita_total)/receita_total

st.write(pd.DataFrame({'receita_total':[receita_total],'receita_total_nova':[receita_total_nova],'dif_percentual':[dif_percentual*100]}))

st.write(f"O valor total das receitas de todos os clientes foi $ {receita_total:,.2f}.\n")
st.write(f"Se fizéssemos uma campanha de marketing para reter os clientes por, pelo menos, mais 12 meses, \
com 100% de adesão dos clientes que abandonariam a empresa, \
o valor total das receitas seria de $ {receita_total_nova:,.2f}, \
ou seja, de {dif_percentual:.2%} a mais.")