from pydantic import BaseModel
from sqlalchemy import Integer,Float
from fastapi import UploadFile, File  #uploadfile is used to handle file uploads in fastapi
#file is used to define file type in uploadfile 


# pydantic models are used to define the structure and validation of data that is sent and received through API endpoints.

#pydantic basemodel class defines the stuctue of data 
# type hints are used to specify the expected data types  

#basemodel data validation ke kaam aata hai matlab jo bhi likha hai usi format me hona chahiye
class Register(BaseModel):
    email:str
    password:str
    role:str

class Login(BaseModel):
    email:str
    password:str

class Expense(BaseModel):
    expense_amt:float
    expense_category:str
    expense_receipt:str
    
class ExpenseUpdate(BaseModel):
    status:str