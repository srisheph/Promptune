from pymongo import MongoClient

def get_db_connection():
    # MongoDB se connect karte hain
    client = MongoClient("mongodb://localhost:27017/")  # MongoDB local server
    db = client["user_db"]  # Database name
    return db
