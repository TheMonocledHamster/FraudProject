import psycopg2
import Const


pc_fn_query = Const.PC_FN
pc_trig_query = Const.PC_TRIG
ft_fn_query = Const.FT_FN
ft_trig_query = Const.FT_TRIG

params = Const.PARAMS
pg_connection = psycopg2.connect(dbname=params["NAME"], user=params["USER"], password=params["PASSWORD"], host=params["HOST"], port=params["PORT"])
db_cursor = pg_connection.cursor()
db_cursor.execute(query=pc_fn_query)
pg_connection.commit()
db_cursor.execute(query=pc_trig_query)
pg_connection.commit()
db_cursor.execute(query=ft_fn_query)
pg_connection.commit()
db_cursor.execute(query=ft_trig_query)
pg_connection.commit()
db_cursor.close()
pg_connection.close()