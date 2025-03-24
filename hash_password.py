from passlib.context import CryptContext

# Password hashing setup4$
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Test password (should match the one in MongoDB)
password = "password123"  
hashed_password = pwd_context.hash(password)

print("Hashed Password: ", hashed_password)  
