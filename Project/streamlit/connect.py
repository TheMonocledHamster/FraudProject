import streamlit as st
import psycopg2 as pg
import json
import os
import pandas as pd
import numpy as np
import sys

# Initialize connection.
# Uses st.cache to only run once.
# @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
conn=''
def init_connection():
    relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
    with open(relpath("..\..\Resources\DBdetails.json"),"r") as deets:
        params = json.load(deets)
    conn=pg.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
    return conn

conn = init_connection()

def getConnDetails():
    return conn

