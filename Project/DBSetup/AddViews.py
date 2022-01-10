import psycopg2
import Const

f_query = Const.F_VIEW
params = Const.PARAMS
pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
db_cursor = pg_connection.cursor()
db_cursor.execute(query=f_query)
pg_connection.commit()
db_cursor.close()
pg_connection.close()