
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine, Base




app = FastAPI(
    title="Library Management API",
    description="Manages books, users, loans, fines, and more",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import routers
from app.routes import user  
from app.routes import book
from app.routes import author
from app.routes import genre
from app.routes import loan
from app.routes import reservation
from app.routes import review
from app.routes import fine

app.include_router(user.router)
app.include_router(book.router)
app.include_router(author.router)
app.include_router(genre.router)
app.include_router(loan.router) 
app.include_router(reservation.router)
app.include_router(review.router)
app.include_router(fine.router) 

@app.get("/")
def root():
    return {"message": "Dummy library Management API"}
