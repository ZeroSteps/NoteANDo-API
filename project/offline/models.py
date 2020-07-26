from project.offline import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(500), unique=True)
    description = db.Column(db.String(500), unique=True)
