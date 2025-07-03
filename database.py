from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship,Session
engine = create_engine("postgres://postgres:rakeshpostgres@localhost/secure_notes", echo=True)

Sessionlocal = sessionmaker(bind=engine)