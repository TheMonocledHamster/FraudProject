import streamlit as st
import psycopg2 as pg

# Initialize connection.
# Uses st.cache to only run once.
@st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return pg.connect(dbname="lfojbrur", user="lfojbrur", password="VzMU1RUOJDYy_xaaFrxurGcrFycCASRe", host="john.db.elephantsql.com", port=5432)

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