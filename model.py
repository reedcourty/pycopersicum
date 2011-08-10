#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlalchemy
import datetime

from sqlalchemy.orm import mapper, sessionmaker

engine = sqlalchemy.create_engine('sqlite:///.db/test.db', encoding='utf8', echo=True)
metadata = sqlalchemy.MetaData()
timesession_table = sqlalchemy.Table('sessions', metadata,
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

class TimeSession(object):
    def __init__(self, start_time, end_time, unit, description, tags):
        self.start_time = start_time
        self.end_time = end_time
        self.unit = unit
        self.description = description
        self.tags = tags
            
    def __repr__(self):
        return "<TimeSession('%s','%s','%s','%s','%s')>" % (self.start_time, self.end_time, self.unit, self.description, self.tags)
    
mapper(TimeSession, timesession_table)

new_timesession = TimeSession(datetime.datetime.now(), datetime.datetime.now()+datetime.timedelta(days=1), 1, u"Leírás", u"cimkék")

SessionMaker = sessionmaker(bind=engine)

session = SessionMaker()

session.add(new_timesession)

new_timesession = TimeSession(datetime.datetime.now(), datetime.datetime.now()+datetime.timedelta(days=1), 1, u"Leírás2", u"cimkék")
session.add(new_timesession)

our_timesession = session.query(TimeSession).filter_by(tags=u'cimkék').all()

print(our_timesession)