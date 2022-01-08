import Const
import psycopg2

SQL_Queries = []
tables = Const.TABLES
params = Const.PARAMS

for table in tables.keys():
    SQL_Queries.append(
        " COPY {} FROM '{}' DELIMITER ',' CSV;".format( table, tables[table] ))

pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
print("Connected...")
db_cursor = pg_connection.cursor()

for query in SQL_Queries:
    db_cursor.execute(query=query)
    pg_connection.commit()

db_cursor.close()
pg_connection.close()
print("Connection Closed.")