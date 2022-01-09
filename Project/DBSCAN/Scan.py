import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import psycopg2
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA

relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))
with open(relpath("..\..\Resources\DBdetails.json"),"r") as deets:
    params = json.load(deets)
pg_conn=psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])

""" Load Data """
X = pd.read_sql("SELECT amount FROM usage_data WHERE use_type = ",pg_conn)
X.fillna(method='ffill', inplace=True)


"""Preprocessing"""
#Scaling data to comparable standard
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#Normalized to Approximate Gaussian Distribution
X_normalized = normalize(X_scaled)
X_normalized = pd.DataFrame(X_normalized)

db_def = DBSCAN(eps=0.5, min_samples=20000)
labels = db_def.labels_


