from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
import pymysql
from flask_login import UserMixin
import os

DATABASE_URL=os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL, echo=True)
class Base(DeclarativeBase):
  pass

class User(Base, UserMixin):
  __tablename__='user'
  id=Column(Integer, primary_key=True, autoincrement=True)
  username=Column(String(100), unique=True, nullable=False)
  password=Column(String(255))
  
  notes = relationship('Notes', back_populates='user')
  
class Notes(Base):
  __tablename__='notes'
  id=Column(Integer, primary_key=True, autoincrement=True)
  notes=Column(Text)
  user_id=Column(Integer, ForeignKey('user.id'))
  
  user = relationship('User', back_populates='notes')
  
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session()

class Crud:
  def __init__(self, session):
    self.session = session
  def read(self, model):
    return self.session.query(model).all()
  def read_by_id(self, model, column_name, column_val):
    return self.session.query(model).filter_by(**{column_name:column_val}).first()
  def add(self, obj):
    self.session.add(obj)
    self.session.commit()
    return 1
  def delete(self, obj):
    self.session.delete(obj)
    self.session.commit()
    return 1
  def update(self, obj):
    self.session.commit()
    return 1