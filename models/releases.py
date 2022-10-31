from config.db import meta
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String


releases = Table(
	'releases', meta,
	Column('id', Integer, primary_key=True),
	Column('date', String(255)),
	Column('title', String(255)),
	Column('description', String(255)),
	Column('link', String(255)),


)