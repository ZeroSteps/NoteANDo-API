from project import db
from project import app
from flask import jsonify
from flask import request
from project import Article
import json

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


@app.route("/api/articles/", methods=["GET"])
def get_all_articles():
    articles = db.session.query(Article).all()
    print(articles)
    return json.dumps(articles, cls=AlchemyEncoder, indent=4, sort_keys=True)


@app.route("/api/post_article/", methods=["POST"])
def post_article():
    title = request.json["title"]
    description = request.json["description"]
    article = Article(title=title, description=description)
    db.session.add(article)
    db.session.commit()
    return jsonify({"is_error": False})


@app.route("/", methods=["GET"])
def main_screen():
    return "Hello, NoteAnDO!"


app.run(debug=True)
