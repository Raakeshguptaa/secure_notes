from fastapi import FastAPI , Depends , HTTPException , status
from models import User,Note
from database import get_db
from sqlalchemy.orm import Session
from schemas import User_model ,Note_model


app = FastAPI()

@app.post("/user",status_code=status.HTTP_201_CREATED)
def add_user(user_data:User_model,db: Session = Depends(get_db)):
    user_data = User(
        username = user_data.username,
        password = user_data.password
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



