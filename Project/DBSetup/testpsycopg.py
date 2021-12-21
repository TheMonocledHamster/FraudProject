import psycopg2
import json

with open("Project\DBdeets.json","r") as deets:
    params = json.load(deets)

pg_connection = psycopg2.connect(**params)

db_cursor = pg_connection.cursor()
with open("Project/InitSchema.sql","r") as schema: 
    db_cursor.execute(schema.read())
