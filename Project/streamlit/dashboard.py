import streamlit as st
import pandas as pd
import numpy as np
import connect
from PIL import Image

def Dashboard():

    conn=connect.getConnDetails()

    
    subscribers=pd.read_sql("SELECT COUNT(*) FROM subscribers",conn)
    transactions=pd.read_sql("SELECT COUNT(*) FROM transactions",conn)
    plans=pd.read_sql("SELECT COUNT(*) FROM plans",conn)
    features=pd.read_sql("SELECT COUNT(*) FROM features",conn)
    usage_data=pd.read_sql("SELECT COUNT(*) FROM usage_data",conn)
    tracking=pd.read_sql("SELECT COUNT(*) FROM tracking",conn)

    st.header('Dashboard')
    st.subheader('Schema : ')
    image = Image.open('../../Resources/Schema.png')
    st.image(image, caption='Schema')
    col1, col2 ,col3,col4,col5,col6= st.columns(6)
    col1.metric("Subscribers",subscribers['count'][0])
    col2.metric("Transactions",transactions['count'][0])
    col3.metric("Plan",plans['count'][0])
    col4.metric("Features",features['count'][0])
    col5.metric("Usage_Data",usage_data['count'][0])
    col6.metric("Tracking",tracking['count'][0])