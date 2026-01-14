from fastapi import APIRouter,Depends,HTTPException
from src.auth import get_current_user
from src.database import get_db
from src  import models
from src import schemas
from sqlalchemy.orm import Session

router=APIRouter()

@router.get("/report")
def expense_report(
    user:models.User=Depends(get_current_user),db:Session=Depends(get_db)):
    
    ex_report=db.query(models.Expense).filter(models.Expense.user_id==user.id).all()

    return ex_report
    

