from project import db
from project import Article

article = Article(title="AOI AOI ANOSadORRRAAA", description="akjdakjdkajdkadajdkajdkajdkajd")
db.session.add(article)
db.session.commit()
