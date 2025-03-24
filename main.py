from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import get_db
from .models import UserDB
from .utils import hash_password, verify_password
from .music import get_recommended_songs  # Now YouTube Music API is used

app = FastAPI()

# Define the User model for request validation
class User(BaseModel):
    username: str
    password: str
    name: str

# Register new user
@app.post("/register")
def register(user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered.")

    hashed_password = hash_password(user.password)
    db_user = UserDB(username=user.username, password=hashed_password, name=user.name)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully!"}

# Login user
@app.post("/login")
def login(user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password):

        raise HTTPException(status_code=400, detail="Invalid username or password.")
    
    return {"message": f"Welcome back, {db_user.name}!"}

# Music recommendation using YouTube Music API
@app.get("/recommend")
def recommend_music(prompt: str):
    genres = get_genres_from_prompt(prompt)
    songs = get_recommended_songs(genres)
    return {"prompt": prompt, "recommendations": songs}

# Helper function for extracting genres from user prompts
def get_genres_from_prompt(prompt):
    mood_genre_mapping = {
        "happy": ["pop", "dance", "indie-pop"],
        "sad": ["acoustic", "blues", "folk"],
        "relaxed": ["chill", "ambient", "lo-fi"],
        "energetic": ["rock", "hip-hop", "electronic"],
        "romantic": ["r-n-b", "soul", "latin"],
        "party": ["edm", "dance", "house"],
    }

    prompt = prompt.lower()
    for mood, genres in mood_genre_mapping.items():
        if mood in prompt:
            return genres
    return ["pop"]  # Default genre

