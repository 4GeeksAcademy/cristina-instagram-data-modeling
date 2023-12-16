import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Nationality(Base):
    __tablename__ = 'nationality'
    id = Column(Integer, primary_key=True)
    country = Column(String(250))
    flag = Column(String(250))

class Residence(Base):
    __tablename__ = 'residence'
    id = Column(Integer, primary_key=True)
    city = Column(String(250))
    country = Column(String(250))
       
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    residence = Column(String(250), nullable=False)
    nationality = Column(String(250), nullable=False)
    residence_id = Column(Integer, ForeignKey('residence.id'))
    residence = relationship(Residence)
    nationality_id = Column(Integer, ForeignKey('nationality.id'))
    nationality = relationship(Nationality)
    
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    comments = Column(String(250))
    likes = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Following(Base):
    __tablename__ = 'follwing'
    id = Column(Integer, primary_key=True)
    comments = Column(String(250))
    likes = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
