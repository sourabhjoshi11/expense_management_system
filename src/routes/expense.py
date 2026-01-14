from fastapi import APIRouter,Depends,HTTPException,Request

from src import models,schemas
from src.database import get_db
from sqlalchemy.orm import Session
from src.auth import generate_jwt,get_current_user

router=APIRouter()

@router.post("/expense")
def user_expense(
    expense_data:schemas.Expense,
    request:Request,
    user:models.User=Depends(get_current_user),
    db:Session=Depends(get_db)
):

    if user.role!="employee":
        raise HTTPException(status_code=404,detail="you are manager" )
    
    receipt=str(request.url)

    new_expense=models.Expense(expense_amt=expense_data.expense_amt,expense_category=expense_data.expense_category,expense_receipt=receipt,user_id=user.id)

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return "Expense added Successfully"

