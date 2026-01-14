from sqlalchemy import Column,String,Integer,ForeignKey,Date
from src.database import Base


from sqlalchemy.orm import relationship 
#relationship is used to define relationship between two tables like one to many many to one etc

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,nullable=False)
    role=Column(String,nullable=False)
    password=Column(String,nullable=False)


class Expense(Base):
    __tablename__="expense"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    expense_amt=Column(Integer,default=0)
    expense_category=Column(String)
    expense_receipt=Column(String,nullable=True)
    status=Column(String,default="pending")

    


