🛠️ How to Run the Project Locally
Follow these steps to get the API up and running on your local machine.

1. Prerequisites
   Ensure you have Python 3.9+ installed on your system. You can check this by running:
   code
   Bash
   python --version
2. Clone the Repository
   code
   Bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd notes_api
3. Create a Virtual Environment
   It is recommended to use a virtual environment to keep dependencies organized.
   On Windows:
   code
   Bash
   python -m venv venv
   .\venv\Scripts\activate
   On macOS/Linux:
   code
   Bash
   python3 -m venv venv
   source venv/bin/activate
4. Install Dependencies
   Install all required libraries using the provided requirements.txt file:
   code
   Bash
   pip install -r requirements.txt
5. Set Up the Database
   This project uses SQLite for easy evaluation. You do not need to perform any manual setup. The database file (notes.db) will be created automatically in the root directory the first time you run the application.
6. Run the Application
   Start the FastAPI server using Uvicorn:
   code
   Bash
   uvicorn app.main:app --reload
   The server will start at: http://127.0.0.1:8000
7. Access API Documentation (Swagger)
   FastAPI automatically generates interactive documentation. Once the server is running, open your browser and visit:
   Swagger UI: http://127.0.0.1:8000/docs (Best for testing)
   ReDoc: http://127.0.0.1:8000/redoc
   🧪 Quick Testing Guide (For the Evaluator)
   Go to /docs.
   Use the /register endpoint to create a new user.
   Use the /login endpoint with the same credentials to receive a JWT access_token.
   Copy the token, click the "Authorize" button at the top of the page, paste the token, and click Authorize.
   Now you can test the /notes endpoints (Create, Read, Update, Delete) as an authenticated user.
   🐳 Running with Docker (Bonus)
   If you have Docker installed, you can run the entire setup with a single command:
   code
   Bash

# Build the image

docker build -t notes-api .

# Run the container

docker run -p 8000:8000 notes-api
The API will then be available at http://localhost:8000/docs.
