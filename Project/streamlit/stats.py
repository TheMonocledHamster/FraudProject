import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
def Stats():
    st.header('Stats')
    chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

    st.line_chart(chart_data)