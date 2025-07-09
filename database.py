from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from config import settings

engine = create_engine(f"postgresql://{settings.database_username}:{settings.database_password}"
                       f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}", echo=True)

Sessionlocal = sessionmaker(bind=engine)
base = declarative_base()


def get_db():
    db = Sessionlocal()

    try:
        yield db

    finally:
        db.close()