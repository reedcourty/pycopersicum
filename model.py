import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///.db/test.db', echo=True)
metadata = sqlalchemy.MetaData()
session_table = sqlalchemy.Table('sessions', metadata,
                                 sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                                 sqlalchemy.Column('start_time', sqlalchemy.DateTime),
                                 sqlalchemy.Column('end_time', sqlalchemy.DateTime),
                                 sqlalchemy.Column('unit', sqlalchemy.Integer),
                                 sqlalchemy.Column('description', sqlalchemy.String),
                                 sqlalchemy.Column('tags', sqlalchemy.String)
                                 )
tags_table = sqlalchemy.Table('tags', metadata,
                                 sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                                 sqlalchemy.Column('name', sqlalchemy.String)
                                 )
metadata.create_all(engine)
