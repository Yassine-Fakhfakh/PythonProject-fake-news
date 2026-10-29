from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(20000), nullable=False)
    date_created = db.Column(db.DateTime, default= lambda: datetime.now(UTC))

    def __repr__(self):
        return '<article %r>' % self.id