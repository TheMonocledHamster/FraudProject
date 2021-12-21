import psycopg2
import json

with open("Resources/DBdeets.json") as deets:
    params = json.load(deets)

conn = psycopg2.connect(**params)

cur = conn.cursor()
with open("InitSchema.sql") as schema: 
    cur.execute(schema.read.replace("\n"," "));
    
