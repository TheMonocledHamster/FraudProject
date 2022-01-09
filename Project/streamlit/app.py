import streamlit as st
import dashboard as db 
import stats as stats
import queries as queries

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