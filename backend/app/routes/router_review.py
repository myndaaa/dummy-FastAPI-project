"""
API routes for Review.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)


@router.post("/", response_model=schemas.ReviewOut, status_code=status.HTTP_201_CREATED)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    """
    Create a new review.
    """
    return crud.crud_review.create_review(db, review)


@router.get("/{review_id}", response_model=schemas.ReviewOut)
def read_review(review_id: int, db: Session = Depends(get_db)):
    """
    Get a review by ID.
    """
    db_review = crud.crud_review.get_review(db, review_id)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review


@router.get("/", response_model=List[schemas.ReviewOut])
def read_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of reviews.
    """
    return crud.crud_review.get_reviews(db, skip=skip, limit=limit)


@router.patch("/{review_id}", response_model=schemas.ReviewOut)
def update_review(review_id: int, review_update: schemas.ReviewUpdate, db: Session = Depends(get_db)):
    """
    Update a review by ID.
    """
    db_review = crud.crud_review.update_review(db, review_id, review_update)
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    return db_review


@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    """
    Delete a review by ID.
    """
    success = crud.crud_review.delete_review(db, review_id)
    if not success:
        raise HTTPException(status_code=404, detail="Review not found")
    return


@router.get("/by_book/{book_id}", response_model=List[schemas.ReviewOut])
def get_reviews_by_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get all reviews for a specific book.
    """
    return crud.crud_review.get_reviews_by_book(db, book_id)


@router.get("/by_user/{user_id}", response_model=List[schemas.ReviewOut])
def get_reviews_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get all reviews by a specific user.
    """
    return crud.crud_review.get_reviews_by_user(db, user_id)
