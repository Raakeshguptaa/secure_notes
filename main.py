from fastapi import FastAPI , Depends , HTTPException , status
from models import User,Note
from database import get_db
from sqlalchemy.orm import Session
from schemas import User_model ,Note_model
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

app = FastAPI()

@app.post("/user",status_code=status.HTTP_201_CREATED)
def add_user(user_data:User_model,db: Session = Depends(get_db)):
    user_data = User(
        username = user_data.username,
        password = pwd_context.hash(user_data.password)
    )

    db.add(user_data)
    db.commit()
    

@app.post("/note",status_code=status.HTTP_201_CREATED)
def add_note(user_notes:Note_model , db:Session= Depends(get_db)):
    user_notes = Note(
        id = user_notes.id,
        title = user_notes.title,
        content = user_notes.content,
        owner_id = user_notes.owner_id
    )

    db.add(user_notes)
    db.commit()

@app.get("/user_detail",status_code=status.HTTP_302_FOUND)
def user_detail(db:Session = Depends(get_db)):

    data = db.query(User).all()

    return ("user_detail",data)

@app.get("/note_detail",status_code=status.HTTP_302_FOUND)
def post_detail(db:Session = Depends(get_db)):
    data = db.query(Note).all()
    return ("note_detail",data)



