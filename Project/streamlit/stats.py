import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import connect

def Stats():

    conn=connect.getConnDetails()

    st.header('Stats')
    countryWise = pd.read_sql('SELECT country,COUNT(*) AS Number FROM subscribers GROUP BY country',conn)
    planWise = pd.read_sql('SELECT plans.plan_id,COUNT(*) As Number FROM plans,subscribers WHERE plans.plan_id=subscribers.cur_plan_id GROUP BY plans.plan_id ORDER BY plans.plan_id ASC',conn)
    priceWise=pd.read_sql('SELECT plans.plan_cost,COUNT(*) As Number FROM plans,subscribers WHERE plans.plan_id=subscribers.cur_plan_id GROUP BY plans.plan_cost ORDER BY plans.plan_cost ASC',conn)
    # st.dataframe(priceWise)
    # st.write(countryWise['number'])

    visType=st.selectbox("Visualization type",['Pie Chart','Bar chart'])
    if visType=='Pie Chart':
        # Country wise users
        countryFig = px.pie(countryWise, values=countryWise['number'], names=countryWise['country'], title='Country wise users')
        st.plotly_chart(countryFig)

        # Plan wise users
        planFig=px.pie(planWise,values=planWise['number'],names=planWise['plan_id'],title='Plan wise users')
        st.plotly_chart(planFig)
        st.dataframe(pd.read_sql("SELECT * from plans",conn))

        # Price wise users
        priceFig=px.pie(priceWise,values=priceWise['number'],names=priceWise['plan_cost'],title='Price wise users')
        st.plotly_chart(priceFig)

    else:
        # Country wise users
        

        countryFig=go.Figure(data=[
        go.Bar(name='Country Wise',x=countryWise['country'], y=countryWise['number'],marker=dict(color = countryWise['number'],
                     colorscale='puor')),])
        st.plotly_chart(countryFig)

        # Plan wise users
        planFig=go.Figure(data=[
        go.Bar(name='planWise',x=planWise['plan_id'], y=planWise['number'],marker=dict(color = planWise['number'],
                     colorscale='puor')),])
        st.plotly_chart(planFig)
        st.dataframe(pd.read_sql("SELECT * from plans",conn))

        # Price wise users
        priceFig=go.Figure(data=[
        go.Bar(name='priceWise',x=priceWise['plan_cost'], y=priceWise['number'],marker=dict(color = priceWise['number'],
                     colorscale='puor')),])
        st.plotly_chart(priceFig)
        

#     st.line_chart(data)
# st.area_chart(data)
# st.bar_chart(data)
# st.pyplot(fig)
# st.altair_chart(data)
# st.vega_lite_chart(data)
# st.plotly_chart(data)
# st.bokeh_chart(data)
# st.pydeck_chart(data)
# st.deck_gl_chart(data)
# st.graphviz_chart(data)
# st.map(data)