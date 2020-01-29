from model import *
from signal import signal, SIGPIPE, SIG_DFL


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_meme(name,category,picture_link,description):
	meme=Meme(name=name,category=category,picture_link=picture_link,description=description)
	session.add(meme)
	session.commit()


def edit_meme(id,name,category,picture_link,description):
	meme=session.query(Meme).filter_by(id=id).one()
	meme.name=name
	meme.category=category
	meme.picture_link=picture_link
	meme.description=description	
	session.commit()

def remove_meme(id1):
	session.remove(get_meme(id1))
	session.commit()

def get_meme(id1):
	return session.query(Meme).filter_by(id=id1).one()
	
def query_all_memes():
	memes = session.query(Meme).all()
	return memes

def add_user(name,email,username,password):
	user=User()
	user.name=name
	user.email=email
	user.username=username
	user.password=password
	session.add(user)
	session.commit()
	

# add_user("loai","loai","loai","loai")

def edit_user(id,name,email,username,password):
	user=session.query(User).filter_by(id=id).one()
	user.name=name
	user.email=email
	user.username=username
	user.password=password

def remove_user(id1):
	session.remove(get_user(id1))
	session.commit()
def get_user(id1):
	return session.query(User).filter_by(id=id1).one()
def query_all_users():
	users = session.query(User).all()
	return users
	
# def add_category(name,picture_link,description):
# 	category=Categories(name=name,picture_link=picture_link,description=description)
# 	session.add(category)
# 	session.commit()

# def edit_category(id,name,picture_link,description):
# 	category=session.query(Categories).filter_by(id=id).one()
# 	category.name=name
# 	category.picture_link=picture_link
# 	category.description=description	
# 	session.commit()

# def remove_category(id1):
# 	session.remove(get_category(id1))
# 	session.commit()

# def get_category(id1):
# 	return session.query(Categories).filter_by(id=id1).one()
	
# def query_all():
# 	categories = session.query(Categories).all()
# 	return categories

signal(SIGPIPE,SIG_DFL) 
