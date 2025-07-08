

from sqlalchemy.orm import Session
from typing import List, Optional

from app import models, schemas


def create_review(db: Session, review: schemas.ReviewCreate) -> models.Review:
    """
    Create a new review.
    """
    db_review = models.Review(
        user_id=review.user_id,
        book_id=review.book_id,
        rating=review.rating,
        comment=review.comment,
        created_at=review.created_at
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_review(db: Session, review_id: int) -> Optional[models.Review]:
    """
    Get a review by ID.
    """
    return db.query(models.Review).filter(models.Review.id == review_id).first()


def get_reviews(db: Session, skip: int = 0, limit: int = 10) -> List[models.Review]:
    """
    Get a list of reviews with pagination.
    """
    return db.query(models.Review).offset(skip).limit(limit).all()


def update_review(db: Session, review_id: int, review_update: schemas.ReviewUpdate) -> Optional[models.Review]:
    """
    Update a review.
    """
    db_review = get_review(db, review_id)
    if not db_review:
        return None

    for key, value in review_update.model_dump(exclude_unset=True).items():
        setattr(db_review, key, value)

    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int) -> bool:
    """
    Delete a review by ID.
    """
    db_review = get_review(db, review_id)
    if not db_review:
        return False

    db.delete(db_review)
    db.commit()
    return True


def get_reviews_by_book(db: Session, book_id: int) -> List[models.Review]:
    """
    Get all reviews for a specific book.
    """
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()


def get_reviews_by_user(db: Session, user_id: int) -> List[models.Review]:
    """
    Get all reviews by a specific user.
    """
    return db.query(models.Review).filter(models.Review.user_id == user_id).all()
