from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect
from os import getenv as v_variable
from dotenv import load_dotenv as load_env
from models import *

load_env()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = v_variable('DATABASE_URL', 'sqlite:///temp.db')
app.config['SECRET_KEY'] = v_variable('SECRET_KEY', 'default_secret_key')
db.init_app(app)


@app.route('/post/', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        article_title = request.form['title'].strip()
        article_content = request.form['content'].strip()
        new_article = Article(title=article_title,content=article_content)
        try:
            db.session.add(new_article)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Une erreur est survenue: {e}'

    else:
        articles = Article.query.order_by(Article.date_created).all()
        return render_template('post.html', articles = articles)



@app.route('/', methods=['POST', 'GET'])
def index():
    articles = Article.query.order_by(Article.date_created).all()
    return render_template('index.html', articles = articles)

@app.route('/delete/<int:id>')
def delete(id):
    article_to_delete = Article.query.get_or_404(id)

    try:
        db.session.delete(article_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f'Une erreur est survenue: {e}'



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    article = Article.query.get_or_404(id)

    if request.method == 'POST':
        article.title = request.form['title']
        article.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    else:
        return render_template('update.html', article=article)

@app.route('/view/<int:id>')
def view(id):
    article = Article.query.get_or_404(id)
    return render_template('view.html', article=article)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)