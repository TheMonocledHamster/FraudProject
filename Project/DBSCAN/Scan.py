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
X = pd.read_sql("SELECT sub_id, amount, COUNT(sub_id) FROM usage_data WHERE use_type='SMS' GROUP BY sub_id,amount",pg_conn)

X = X.drop('sub_id',axis=1)
X.fillna(method='ffill', inplace=True)


"""Preprocessing"""
#Scaling data to comparable standard
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
#Normalized to Approximate Gaussian Distribution
X_normalized = normalize(X_scaled)
X_normalized = pd.DataFrame(X_normalized)

""" Dimensional Fitting """
pca = PCA(n_components = 2)
X_principal = pca.fit_transform(X_normalized)
X_principal = pd.DataFrame(X_principal)
X_principal.columns = ['P1', 'P2']

db_def = DBSCAN(eps=0.3, min_samples=300).fit(X_principal)
labels = db_def.labels_

colors = {}
colors[0] = 'r'
colors[1] = 'g'
colors[2] = 'b'
colors[-1] = 'k'

color_vector = [colors[label] for label in labels]

r = plt.scatter(X_principal['P1'], X_principal['P2'], color ='r')
g = plt.scatter(X_principal['P1'], X_principal['P2'], color ='g')
b = plt.scatter(X_principal['P1'], X_principal['P2'], color ='b')
k = plt.scatter(X_principal['P1'], X_principal['P2'], color ='k')

plt.figure(figsize=(9,9))
plt.scatter(X_principal['P1'], X_principal['P2'], c=color_vector)

plt.legend((r,g,b,k),('UG0','UG1','UG2','Frauds'))

plt.show()