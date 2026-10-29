PythonProject Fake News

PythonProject Fake News is a web app made in 2024 with the sole purpose of managing news articles, specifically "Fake News". This project was designed to explore backend development mechanics with Flask while providing an AI-generated style interface.
Ps: It's a partially AI-generated style—even if I'm not a CSS dev and find many difficulties with it, I tried to make something more human. I tweaked the CSS by adjusting color values and adding a dynamic Day/Night theme system using CSS variables (`:root`) and js.
Credits

This project is inspired by the work of Jake Rieger. I used this project to learn the fundamentals of Flask and a little bit of SQL, then developed the entire backend logic following the advice in his YouTube video. I also wanted to improve on the original by changing the model and upgrading the code with my newly acquired skills.

Special thanks to Jake Rieger for contributing to my growth as a developer!
https://github.com/jakerieger/FlaskIntroduction (I finaly found it)

Features

CRUD Methods:

GET: Displaying the list and individual reading of articles.

POST: Creating new articles.

UPDATE: Secure modification of existing titles and content.

DELETE: Ability to remove articles from the database.

I tried to make it easy for everyone to get started:

How to try it for yourself:

Clone the repository:

git clone https://github.com/Yassine-Fakhfakh/PythonProject-fake-news

Create and activate your virtual environment:

python -m venv .venv
On Windows:
.venv\Scripts\activate

Create the .env file with :

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///news.db 

Fun fact: when trying to clone this repo myself after a while, I completely forgot to create the .env file.

Install dependencies:

pip install -r requirements.txt

Configuration:
Create a .env file at the root with:

SECRET_KEY=your_secret_key
DATABASE_URL=your_data_base

Run the application:

python app.py