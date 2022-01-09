import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def Dashboard():
    st.header('Dashboard')
    st.subheader('Schema : ')
    image = Image.open('../../Resources/Schema.png')
    st.image(image, caption='Schema')
