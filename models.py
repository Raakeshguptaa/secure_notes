from database import engine
from database import base , Column , Integer,String,ForeignKey , relationship

class User(base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    username = Column(String,nullable=False)
    password = Column(String,nullable=False)
    notes = relationship("Note",back_populates="owner")


class Note(base):
    __tablename__ = "notes"
    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    owner_id =Column(Integer,ForeignKey("users.id"))
    owner = relationship("User",back_populates="notes")

base.metadata.create_all(engine)