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

########################################################################

st.header('Análise Exploratória de Dados com Visualização Gráfica')


#PIE CHART
st.subheader('*Churn rate*')
labels = ['No','Yes']
values = data['Churn'].value_counts()

st.plotly_chart(go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0.1, 0])]))

st.write((f'O churn rate da empresa é de 26,5%.'))

# BAR CHART # BOXPLOT

##########################################################################

st.subheader('Alguns *Insights*')

st.write("- Clientes que tem parceiros (Partner) e dependentes (Dependents) tendem a permanecer mais tempo utilizando os serviços da empresa (tenure).")

st.write(" - Clientes que possuem serviços online (OnlineBackup, OnlineSecurity, StreamingTV, StreamingMovies) \
         e serviços de assistência (TechSupport) também tendem a permanecer mais tempo como clientes da empresa (tenure)")

st.write(" - Clientes que utilizam serviços de proteção (DeviceProtection), streaming (StreamingTV e StreamingMovies) \
          e recebem a fatuar por e-mail trazem maiores receitas mensais do que quem não utiliza esses serviços")


option_num = st.selectbox(
    'Selecione uma das variáveis abaixo:',
    (var_num))

option_cat1 = st.selectbox(
    'Selecione uma das variáveis abaixo:',
    (var_cat))

tab_distribuicao, tab_boxplot = st.tabs(["Distribuição", "Boxplot"])

with tab_distribuicao:

    st.plotly_chart(px.histogram(data, option_num))

with tab_boxplot:

    mostrar_churn = st.checkbox("Mostrar gráfico com Churn")

    if mostrar_churn:
        st.plotly_chart(px.box(data, x=option_cat1, y=option_num, color="Churn"))
    
    else:
        st.plotly_chart(px.box(data, x=option_cat1, y=option_num))
        
            


# BAR PLOT

st.subheader('*Insights* relacionados ao Churn')

option_cat = st.selectbox(
    'Selecione uma das variáveis abaixo: ',
    (var_cat))

st.write('- Há muito menos idosos, no entanto, quase metade deles irá deixar a empresa em algum momento.')
st.write('- Clientes que possuem fibra óptica (Fiber optic) churnam com mais facilidade, comparado com outros \
         serviços de internet (InternetService).')
st.write('- Clientes que não possuem serviços online (OnlineSecurity, OnlineBackup) churnam mais do que clientes que possuem.')
st.write('- Quase metade dos clientes que não possuem suporte técnico (TechSupport) churnam.')
st.write('- Clientes que utilizam meios eletrônicos para pagamentos churnam mais que clientes que utilizam outros meios.')

st.plotly_chart(px.histogram(data, x=option_cat, color="Churn", barmode='group'))