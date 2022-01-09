import streamlit as st
import pandas as pd
import os
import connect 

def Queries():

    conn=connect.getConnDetails()


    st.header('Queries')
    col1,col2,col3,col4,col5=st.columns(5)
    table='subscribers'
    column='All Columns'
    subCols=["All Columns",'sub_id','full_name','created_at','country','phone_no','cur_plan_id']
    transCols=["All Columns",'trans_id','sub_id','trans_type','created_at','country','buy_plan_id']
    planCols=["All Columns",'plan_id','plan_data','validity','plan_cost','feature_id','postpaid']
    featuresCols=["All Columns",'feature_id','sms','netflix','primevideo','hotstar']
    usageDataCols=["All Columns",'usage_id','sub_id','use_type','usage_time','amount']
    trackPlanCols=["All Columns",'trans_id','upgrade','cost_diff']
    with col1:
        table=st.selectbox("Select Table",['subscribers','transactions','plans','tracking','usage_data','features'])

    with col2:
        if table=='subscribers':
            column=st.selectbox("Select Column",subCols)
        elif table=='transactions':
            column=st.selectbox("Select Column",transCols)
        elif table=='plans':
            column=st.selectbox("Select Column",planCols)
        elif table=='features':
            column=st.selectbox("Select Column",featuresCols)
        elif table=='usage_data':
            column=st.selectbox("Select Column",usageDataCols)
        else:
            column=st.selectbox("Select Column",trackPlanCols)
        
    with col3:
        where=''
        whereFilter=st.text_input('WHERE')
        
    with col4:
        orderBy=''
        order=st.text_input('ORDER BY')

    with col5:
        st.header('')
        if column=='All Columns':
            column='*'
        if order!='':
            orderBy='ORDER BY '+order
        if whereFilter!='':
            where='WHERE '+whereFilter
        st.button('Submit Query',key='queryCallback',on_click=execQuery,args=('SELECT '+column+' FROM '+table+' '+where+' '+orderBy,conn))

    
    
def execQuery(sql_query,conn):
        df=pd.read_sql(sql_query,conn)
        st.dataframe(df)