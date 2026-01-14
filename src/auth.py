import jwt 
from src.models import User
from src.database import get_db
from fastapi import Depends,HTTPException   
from sqlalchemy.orm import Session 

secret_key="MY"
algorithm="HS256"

def generate_jwt(payload):
    to_encode=payload.copy()
    token=jwt.encode(to_encode,secret_key,algorithm=algorithm)

    return token

def get_current_user(token,db:Session=Depends(get_db)):
    decoded_jwt=jwt.decode(token,secret_key,algorithms=[algorithm])

    user_email=decoded_jwt.get("sub")

    if not user_email:
        raise HTTPException(status_code=404,detail="could not validate user")
    
    user=db.query(User).filter(User.email==user_email).first()

    if not user:
        return "user not found"
    
    return user
