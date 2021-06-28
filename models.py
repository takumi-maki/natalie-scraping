# coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date
from database import Base
from datetime import datetime as dt

#Table情報
class Data(Base):
    #TableNameの設定
    __tablename__ = "data"
    #Column情報を設定する
    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    summary = Column('summary', String)
    score = Column('score', Integer)
    time = Column('time', String)    
    timestamp = Column(DateTime, default=dt.now())

    def __init__(self, title=None, summary=None, score=None, time=None, timestamp=None):
        self.title = title
        self.summary = summary
        self.score = score
        self.time = time
        self.timestamp = timestamp
