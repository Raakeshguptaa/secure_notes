from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgres://postgres:rakeshpostgres@localhost/secure_notes", echo=True)

Sessionlocal = sessionmaker(bind=engine)
base = declarative_base()