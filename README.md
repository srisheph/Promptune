# Promptune
AI Recommendation Music System
Promptune is an interactive music recommendation system that suggests personalized playlists based on user mood or input prompts. It uses the data for fetching song recommendations and integrates with MongoDB for user authentication and registration.
Features
●	User Authentication: Sign up and log in to get personalized music recommendations.

●	Music Recommendations: Based on user prompts, get song suggestions from YouTube Music.

●	Clean and Easy-to-use UI: Built using Streamlit for a beautiful user interface.

●	Password Hashing: Secure user password management with bcrypt.
________________________________________
Setup Instructions
Requirements
Ensure you have the following installed:
1.	Python 3.7+
2.	MongoDB running locally (or change connection string for remote).
3.	Dependencies from requirements.txt (you can install these with pip).


1. Create a Virtual Environment (Optional but Recommended)
Create a new virtual environment using venv (or another tool like conda).
python -m venv promptune-env

Activate it:
●	Windows: promptune-env\Scripts\activate

●	Linux/Mac: source promptune-env/bin/activate

3. Install the dependencies
Run the following command to install all the dependencies listed in requirements.txt.
pip install -r requirements.txt

4. Set up MongoDB
If MongoDB is running locally, no changes are required in your code for the database connection. Just make sure MongoDB is up and running on your machine.

________________________________________
Usage
1. Run the FastAPI server
uvicorn main:app --reload

This will start the FastAPI server. You can navigate to the URL (http://127.0.0.1:8000) to use the backend API.
2. Run the Streamlit UI
streamlit run app.py

This will start the Streamlit frontend. You'll be able to access the app through your browser. The main page will allow you to log in and get music recommendations.
________________________________________
How It Works
1. User Registration
●	Users can register with their username, password, and name.

●	Passwords are securely hashed using bcrypt.

●	Data is stored in MongoDB in the database named user_db  under the users collection.
3. User Login
●	After registering, users can log in with their username and password.

●	The system authenticates by verifying the password using bcrypt.

●	Upon successful login, users can access music recommendations.
![image](https://github.com/user-attachments/assets/03e039c4-4e41-4ea1-8446-487dfe6a97cc)

●	 
3. Music Recommendations
●	After logging in, users can enter a mood or prompt (e.g., "happy", "sad", "party").

●	Based on the prompt, the app fetches music suggestions from the user’s data.

●	It returns a list of songs with their title, artist, and a link to listen on YouTube Music.
![image](https://github.com/user-attachments/assets/3e8920c8-ffaf-4f77-ac72-88d371576018)

________________________________________
Code Overview
1. app.py - Streamlit UI
●	Contains the frontend built with Streamlit.
●	Handles user registration, login, and display of music recommendations.
2. database.py - MongoDB Connection
●	Defines the connection to the MongoDB database and handles user authentication queries.
3. music.py - Music Recommendation Logic
●	Uses the YouTube Music API to fetch songs based on the user's prompt.
●	Formats the song data to show the title, artist, and YouTube link.
4. utils.py - User Registration and Authentication
●	Handles user registration and password hashing using Passlib.
●	Also handles user authentication by verifying the hashed password stored in MongoDB.
5. requirements.txt - Dependencies
●	Lists all the Python packages required to run the app. Ensure that you have them installed in your environment.
________________________________________
Technologies Used
●	Streamlit: For building the UI.

●	FastAPI: For the backend API.

●	MongoDB: For storing user data.

●	YTMusic API: For fetching song recommendations.

●	Passlib (bcrypt): For secure password hashing and authentication.
________________________________________
Future Improvements
●	Recommendation Algorithm: Enhance the recommendation system with machine learning to analyze user preferences over time.

●	Playlist Generation: Allow users to generate a full playlist from the recommended songs.

●	Cross-Platform: Extend the app to support other music services like Spotify.
![image](https://github.com/user-attachments/assets/a865165c-205b-4f14-92bc-6e25db31898e)
 
________________________________________
Contact
For any questions, feel free to reach out to:
●	Email: srivastavashephali02@gmail.com
