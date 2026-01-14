from fastapi import FastAPI
from src.database import Base,engine
from src.routes import auth,expense,report,manager
from src import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)  
#base class contains the metadata object that collect all the table definition (table name,column etcof class that inherit from it then metadata is used to generate actual database schema)

app.include_router(auth.router,prefix="/auth")
app.include_router(expense.router,prefix="/expense")
app.include_router(report.router,prefix="/report")
app.include_router(manager.router,prefix="/manager")