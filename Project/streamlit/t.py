import streamlit as st
import psycopg2 as pg
import json
import os
import sys

# Initialize connection.
# Uses st.cache to only run once.
@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})

def init_connection():
    relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
    with open(relpath("..\..\Resources\DBdetails.json"),"r") as deets:
        params = json.load(deets)
    return pg.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])


conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from features;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")