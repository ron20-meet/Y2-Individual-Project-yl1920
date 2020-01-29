from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from signal import signal, SIGPIPE, SIG_DFL

Base = declarative_base()

class Meme(Base):
	__tablename__="memes"
	id=Column(Integer,primary_key=True)
	name=Column(String)
	picture_link=Column(String)
	category=Column(String)

# class Categories(Base):
# 	__tablename__="categories"
# 	id=Column(Integer,primary_key=True)
# 	name=Column(String)
# 	picture_link=Column(String)
	
class User(Base):
	__tablename__="user"
	id=Column(Integer ,primary_key=True)
	name = Column(String)
	username=Column(String)
	email=Column(String)
	password=Column(String)
	#favorites=Column(String)



		#def __init__(name,email,username,password):
			#self.name = name
			#self.email= email
			#self.username = username
			#self.password = password		

signal(SIGPIPE,SIG_DFL) 
