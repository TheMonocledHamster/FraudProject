import streamlit as st
import dashboard as db 
import stats as stats
import queries as queries
st.sidebar.title(
    "FraudProject",
)
page=st.sidebar.radio(
    "",
    ['Dashboard','Stats','Queries']
)

if(page=='Dashboard'):
    db.Dashboard()
    
if(page=='Stats'):
    stats.Stats()

if(page=='Queries'):
    queries.Queries()