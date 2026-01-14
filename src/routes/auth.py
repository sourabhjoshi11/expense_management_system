from fastapi import APIRouter,Depends,HTTPException
from src.models import User,Expense 
from src.schemas import Register,Login
from src.database import get_db
from src.auth import generate_jwt
from sqlalchemy.orm import Session



router=APIRouter()

@router.post("/register")
def register_user(user:Register,db:Session=Depends(get_db)):
    existing=db.query(User).filter(User.email==user.email).first()
    #select user from User table where id==user.id

    if existing:
        raise HTTPException(status_code=404,detail="user already exist")

    new_user=User(email=user.email,password=user.password,role=user.role)

    db.add(new_user)
    db.commit()

    return "New User Registered Successfully"

@router.post("/login")
def user_login(user:Login,db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.email==user.email).first()

    if not db_user or not(user.password,db_user.password):
        raise HTTPException(status_code=404,detail="Invalid credentials")
    
    token= generate_jwt({"sub":db_user.email})
    
    print("User logged in successfully")

    return {"access_token":token,"token_type":"bearer"}
