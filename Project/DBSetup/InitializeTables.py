import psycopg2
import json
import os

relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))

with open(relpath("..\DBdetails.json"),"r") as deets:
    params = json.load(deets)

pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
pg_connection.set_session(autocommit=True)
db_cursor = pg_connection.cursor()
with open(relpath("InitSchema.sql"),"r") as schema:
    db_cursor.execute(schema.read())
