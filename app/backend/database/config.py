# import
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# local import
from app.backend.utils.constants import Constants as cns


# define engine object
engine: object = create_engine(url=cns.CONN_STRING.value, echo=False)

# define session object
session: object = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# define BASE class for models
BASE = declarative_base()


# db session controller
def Session_Controller() -> None:
    """
    Dependency function to provide a SQLAlchemy session for database operations.

    This function:
    - Creates a new session instance.
    - Yields it for use in routes or services.
    - Ensures the session is properly closed after use.

    Yields:
        Session: A SQLAlchemy session instance.
    """

    # instance session
    database = session()
    # yield session when needed
    try:
        yield database
    finally:
        database.close()
