"""
Schemas package
"""

from .user import (
    UserBase,
    UserCreate,
    UserUpdate,
    UserInDB,
    UserOut
)

from .author import (
    AuthorBase,
    AuthorCreate,
    AuthorUpdate,
    AuthorInDB,
    AuthorOut
)

from .book import (
    BookBase,
    BookCreate,
    BookUpdate,
    BookInDB,
    BookOut
)

from .genre import (
    GenreBase,
    GenreCreate,
    GenreUpdate,
    GenreInDB,
    GenreOut
)

from .loan import (
    LoanBase,
    LoanCreate,
    LoanUpdate,
    LoanInDB,
    LoanOut
)

from .reservation import (
    ReservationBase,
    ReservationCreate,
    ReservationUpdate,
    ReservationInDB,
    ReservationOut
)

from .fine import (
    FineBase,
    FineCreate,
    FineUpdate,
    FineInDB,
    FineOut
)

from .review import (
    ReviewBase,
    ReviewCreate,
    ReviewUpdate,
    ReviewInDB,
    ReviewOut
)


__all__ = [
    "UserBase", "UserCreate", "UserUpdate", "UserInDB", "UserOut",
    "AuthorBase", "AuthorCreate", "AuthorUpdate", "AuthorInDB", "AuthorOut",
    "BookBase", "BookCreate", "BookUpdate", "BookInDB", "BookOut",
    "GenreBase", "GenreCreate", "GenreUpdate", "GenreInDB", "GenreOut",
    "LoanBase", "LoanCreate", "LoanUpdate", "LoanInDB", "LoanOut",
    "ReservationBase", "ReservationCreate", "ReservationUpdate", "ReservationInDB", "ReservationOut",
    "FineBase", "FineCreate", "FineUpdate", "FineInDB", "FineOut",
    "ReviewBase", "ReviewCreate", "ReviewUpdate", "ReviewInDB", "ReviewOut"
]
