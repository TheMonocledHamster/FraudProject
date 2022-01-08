import psycopg2
import Const

query = """SELECT
  'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;' 
from
  pg_tables WHERE schemaname = 'public';"""

params = Const.PARAMS
pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
db_cursor = pg_connection.cursor()
db_cursor.execute(query=query)
pg_connection.commit()
db_cursor.close()
pg_connection.close()