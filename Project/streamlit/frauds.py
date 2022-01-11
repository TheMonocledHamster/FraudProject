import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from streamlit.elements.number_input import Number
import connect

def Frauds():

    conn=connect.getConnDetails()
    
    st.header('Frauds')

    st.write('Perpetrators')
    fraudsDetails = pd.read_sql("SELECT * FROM frauds",conn)
    st.dataframe(fraudsDetails)

    countryWise = pd.read_sql('SELECT fraud_locale AS Location,COUNT(*) AS Count FROM frauds GROUP BY fraud_locale',conn)
    countryFraudPie = px.pie(countryWise, values=countryWise['count'], names=countryWise['location'],title='Country-wise Frauds')
    st.plotly_chart(countryFraudPie)

    st.write('DBSCAN Results')
    DBSCAN = Image.open('../../Resources/DBSCAN.png')
    st.image(DBSCAN,caption='Analysis')
