from sqlalchemy import create_engine       #sqlalchemy provides a flexible way to connect with db 
#it helps to write sql queries in python classes and object instead of writing raw sql queries
from sqlalchemy.orm import sessionmaker, declarative_base
import os

 #orm is object relational mapper it helps to map python class and object to database table it enables us to interact with db using obj and class
#  orm automatically convert object operation or queries into sql statement 
  #session maker interact with db ,declarative base defines how our data looks like and how it will be going to map with database

database_url='postgresql://postgres:1234@db:5432/postgres'

DB_URL = os.getenv("DATABASE_URL", database_url)

engine = create_engine(DB_URL) # create to connect the db


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#sesssionmaker interatcs with database  , autocommit false means changes will not be saved automatically we have to commit them manually

#bind=engine means it will use the engine we created to connect to db

Base=declarative_base()

def get_db():
    db = SessionLocal()   #to interact with database for each request
    try: 
        yield db          
    finally:
        db.close()
