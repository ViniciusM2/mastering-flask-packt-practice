from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)


@app.route('/')
def home():
    return '<h1>Hello World!!!</h1><h2>Tudo bem?</h2>'


if __name__ == '__main__':
    app.run()

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='subquery'
    )

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __init__(self, title):
        self.title = title
    
    def __repr__(self):
        return "<Post '{}'>".format(self.title)

class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __init__(self,name):
        self.text = text

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])


