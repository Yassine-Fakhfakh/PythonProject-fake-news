PythonProject Fake News

PythonProject Fake News is a web app made in 2025 with the sole purpose of managing news articles, specifically "Fake News". This project was designed to explore backend development mechanics with Flask while providing an AI-generated "Neon/Cyberpunk" style interface.

Credits

This project is inspired by the work of Jake Rieger. I used this project to learn the fundamentals of Flask, then developed the entire backend logic following the advice in his YouTube video.

Special thanks to Jake Rieger for contributing to my growth as a developer!

Features

CRUD Methods:

GET: Displaying the list and individual reading of articles.

POST: Creating new articles.

UPDATE: Secure modification of existing titles and content.

DELETE: Ability to remove articles from the database.

Project Evolution

Update of July 2025: Addition of a new visual style.

Latest Updates (27/04/2026):

Security: Implementation of environment variables (.env) to protect the SECRET_KEY and database URI.

Refactoring: Code optimization for better performance.

How to try this app

I tried to make it easy for everyone to get started:

Clone the repository:

git clone https://github.com/Yassine-Fakhfakh/PythonProject-fake-news

Create and activate your virtual environment:

python -m venv .venv
# On Windows:
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Configuration:
Create a .env file at the root with:

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///article.db


Run the application:

python app.py


