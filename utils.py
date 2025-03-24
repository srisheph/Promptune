

from passlib.context import CryptContext
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["user_db"]
users_collection = db["users"]

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Register User
def register_user(username, password, name):
    if users_collection.find_one({"username": username}):
        return "Username already exists!"
    
    hashed_password = pwd_context.hash(password)
    users_collection.insert_one({"username": username, "password": hashed_password, "name": name})
    return f"User {username} registered successfully!"


# Authenticate User
def authenticate_user(username, password):
    user = users_collection.find_one({"username": username})
    if user and pwd_context.verify(password, user["password"]):
        return True
    return False

# Get Recommended Songs based on prompt (search in YouTube Music API)
from ytmusicapi import YTMusic

# Initialize YouTube Music API
ytmusic = YTMusic()

def format_song_data(song):
    return {
        "title": song.get("title", "Unknown"),
        "artist": song["artists"][0]["name"] if song.get("artists") else "Unknown",
        "url": f"https://music.youtube.com/watch?v={song['videoId']}" if song.get("videoId") else None
    }

def get_recommended_songs(prompt):
    search_results = ytmusic.search(prompt, filter="songs")
    return [format_song_data(song) for song in search_results[:7]]



