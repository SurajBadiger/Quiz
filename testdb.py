import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy.orm import mapper

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base



url="sqlite:///quiz.db"
engine = sqlalchemy.create_engine(url)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


print("connected to database")
from sqlalchemy import Column,MetaData,Table,Text
metadata=MetaData()


class Question(Base):
    __tablename__ = 'questions'
    question = Column(Text)
    id =Column(Integer,primary_key=True)
    op1 = Column(Text)
    op2 = Column(Text)
    op3 = Column(Text)
    op4 = Column(Text)
    answer  = Column(Text)

    def __init__(self, question,op1,op2,op3,op4,answer):
        self.question = question
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.answer = answer

data = db_session.query(Question).all()
print(data)