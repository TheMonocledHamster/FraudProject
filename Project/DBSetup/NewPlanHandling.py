import psycopg2
import Const


fn_query = Const.PC_FN
trig_query = Const.PC_TRIG
params = Const.PARAMS
pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
db_cursor = pg_connection.cursor()
db_cursor.execute(query=fn_query)
pg_connection.commit()
db_cursor.execute(query=trig_query)
pg_connection.commit()
db_cursor.close()
pg_connection.close()