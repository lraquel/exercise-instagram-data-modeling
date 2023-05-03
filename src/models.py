import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), nullable=False)
    follower = relationship("Follower")
    post = relationship("Post")
    author = relationship("Comment")


class Follower(Base):
    __tablename__= "follower"
    id = Column(primary_key=True)
    user_from_id = Column(ForeignKey("user.id"))
    user_to_id = Column(ForeignKey("user.id"))


class Post(Base):
    __tablename__="post"
    id = Column(primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    media = relationship("Media")
    comment = relationship("Comment")


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(String(205))
    url = Column(String(250))
    post_id = Column(ForeignKey("post.id"))
    

class Comment(Base):
    __tablename__="comment"
    id = Column(Integer,primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(ForeignKey("user.id"))
    post_id = Column(ForeignKey("post.id"))
    

   

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
