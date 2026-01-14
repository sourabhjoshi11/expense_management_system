from fastapi import APIRouter, Depends, HTTPException, status
from src import models, schemas
from src.database import get_db 
from sqlalchemy.orm import Session 
from src.auth import get_current_user   

router = APIRouter()

@router.put("/manager/{emp_id}")
def approve_expense(
     emp_id: int,
     payload: schemas.ExpenseUpdate,
     user: models.User = Depends(get_current_user),
     db: Session = Depends(get_db)

):
    print("here")
    if user.role != "manager":
        raise HTTPException(status_code=404, detail="You are not authorized as a manager")
 
    expense_request = db.query(models.Expense).filter(
        models.Expense.user_id == emp_id
    ).first()
      
    
    if not expense_request:
        raise HTTPException(status_code=404, detail="Expense record not found for this employee")


    
    expense_request.status = payload.status

    db.commit()
    db.refresh(expense_request)

    return "work done"

