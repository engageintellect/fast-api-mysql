from curses import meta
from sqlalchemy import create_engine, MetaData
engine = create_engine('mysql+pymysql://root@localhost:3306/py_crud')
meta=MetaData()
con=engine.connect()

if con:
	print('-------------------------------')
	print('Database connection successful.')
	print('-------------------------------')
else:
	print('-------------------------------')
	print('Database connection failed.')
	print('-------------------------------')