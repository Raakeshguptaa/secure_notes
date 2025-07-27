from fastapi import FastAPI , Depends , HTTPException , status
from models import User,Note
from database import get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from schemas import User_model ,Note_model , Login_user
from passlib.context import CryptContext


SECRET_KEY = "myjwtsecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")




def verify_password(plan_password,hashed_password):
    return pwd_context.verify(plan_password,hashed_password)

def get_user(db, username: str):
    return db.query(User).filter(User.username == username).first()


def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=username)
    if user is None:
        raise credentials_exception
    return user


@app.get("/")
def show():
    return {"message":"hello world"}
@app.post("/login")
def login(log_user : Login_user,db:Session= Depends(get_db)):

    user = db.query(User).filter(User.username == log_user.username).first()

    if not user:
        raise HTTPException(status_code=401,detail="user not verified")
    
    if not verify_password(log_user.password,user.password):
        raise HTTPException(status_code=401,detail="incorrect password")
    
    access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": access_token, "token_type": "bearer"}



# regitering user cridential

@app.post("/user",status_code=status.HTTP_201_CREATED)
def add_user(user_data:User_model,db: Session = Depends(get_db)):
    user_data = User(
        username = user_data.username,
        password = pwd_context.hash(user_data.password)
    )

    db.add(user_data)
    db.commit()
    db.refresh(user_data)

# adding notes

@app.post("/note",status_code=status.HTTP_201_CREATED)
def add_note(user_notes:Note_model , db:Session= Depends(get_db),current_user : User = Depends(get_current_user)):
    user_notes = Note(
        id = user_notes.id,
        title = user_notes.title,
        content = user_notes.content,
        owner_id = current_user.id
    )

    db.add(user_notes)
    db.commit()
    db.refresh(user_notes)
    return {"msg": "Note added", "note_id": user_notes.id}
    


@app.get("/user_detail",status_code=status.HTTP_302_FOUND)
def user_detail(db:Session = Depends(get_db)):

    data = db.query(User).all()

    return ("users_detail",data)

@app.get("/note_detail",status_code=status.HTTP_302_FOUND)
def note_detail(current_user : User = Depends(get_current_user)):
    return [{"title": note.title,"content":note.content} for note in current_user.notes]



@app.get("/notes/{note_id}")
def read_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(Note.id == note_id, Note.owner_id == current_user.id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"title": note.title, "content": note.content}