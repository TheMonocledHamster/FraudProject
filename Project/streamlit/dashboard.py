import streamlit as st
import pandas as pd
import numpy as np
import time
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

    st.title('Dashboard')
    st.header('Schema : ')
    image = Image.open('../../Resources/Schema.png')
    st.image(image, caption='Schema')
    
    emptySpace()

    st.header("Number of entries in each table")
    col1, col2 ,col3,col4,col5,col6= st.columns(6)
    col1.metric("Subscribers",subscribers['count'][0])
    col2.metric("Transactions",transactions['count'][0])
    col3.metric("Plan",plans['count'][0])
    col4.metric("Features",features['count'][0])
    col5.metric("Usage_Data",usage_data['count'][0])
    col6.metric("Tracking",tracking['count'][0])

    emptySpace()

    st.header("Description of Tables")
    col7,col8,=st.columns(2)
    with col7:
        col7.subheader("Subscribers :")
        col7.dataframe(pd.read_sql("SELECT column_name as Columns,is_nullable as NULL,udt_name as Type  FROM information_schema.COLUMNS  WHERE TABLE_NAME = 'subscribers'",conn))
        
        col7.subheader("Plans :")
        col7.dataframe(pd.read_sql("SELECT column_name as Columns,is_nullable as NULL,udt_name as Type  FROM information_schema.COLUMNS  WHERE TABLE_NAME = 'plans'",conn))
        
        col7.subheader("Usage_Data :")
        col7.dataframe(pd.read_sql("SELECT column_name as Columns,is_nullable as NULL,udt_name as Type  FROM information_schema.COLUMNS  WHERE TABLE_NAME = 'usage_data'",conn))
    
    
    with col8:
        col8.subheader("Transactions :")
        col8.dataframe(pd.read_sql("SELECT column_name as Columns,is_nullable as NULL,udt_name as Type  FROM information_schema.COLUMNS  WHERE TABLE_NAME = 'transactions'",conn))
    
        col8.subheader("Features :")
        col8.dataframe(pd.read_sql("SELECT column_name as Columns,is_nullable as NULL,udt_name as Type  FROM information_schema.COLUMNS  WHERE TABLE_NAME = 'features'",conn))
    
        col8.subheader("Tracking :")
        col8.dataframe(pd.read_sql("SELECT column_name as Columns,is_nullable as NULL,udt_name as Type  FROM information_schema.COLUMNS  WHERE TABLE_NAME = 'tracking'",conn))

    

def emptySpace():
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")