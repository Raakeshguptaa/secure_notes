from sqlalchemy import create_engine ,Integer , String , Float , Column , ForeignKey 
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql://postgres:rakeshpostgres@localhost:5432/secure_notes", echo=True)

Sessionlocal = sessionmaker(bind=engine)
base = declarative_base()


def get_db():
    db = Sessionlocal()

    try:
        yield db

    finally:
        db.close()