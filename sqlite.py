from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String

 
engine = create_engine('sqlite:///users.db', echo=True)
 
metadata = MetaData(bind=engine)
 
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('username', String(40)),
                    Column('passwordz', String),
                    )

# create tables in database
metadata.create_all()





