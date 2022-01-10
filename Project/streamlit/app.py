import streamlit as st
import dashboard as db 
import stats 
import queries 
import frauds 

st.set_page_config(layout="wide")

with st.sidebar:
    st.title(
    "FraudProject",
    )
    page=st.selectbox(
    "",
    ['Dashboard','Stats','Frauds','Queries']
    )

if(page=='Dashboard'):
    db.Dashboard()
    
if(page=='Stats'):
    stats.Stats()

if(page=='Queries'):
    queries.Queries()

if(page=='Frauds'):
    frauds.Frauds()