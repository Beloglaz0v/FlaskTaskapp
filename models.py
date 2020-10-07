from app import db, session, Base
from sqlalchemy.orm import relationship
from flask_jwt_extended import create_access_token
from datetime import timedelta, datetime
from passlib.hash import bcrypt


class Status(Base):
    __tablename__ = 'statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)


class Task(Base):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Integer, db.ForeignKey('statuses.id'))
    deadline = db.Column(db.Date)


class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    tasks = relationship('Task', backref='user', lazy=True)

    def __init__(self, **kwargs):
        self.login = kwargs.get('login')
        self.password = bcrypt.hash(kwargs.get('password'))

    def get_token(self, expite_time=24):
        expite_delta = timedelta(expite_time)
        token = create_access_token(
            identity=self.id, expires_delta=expite_delta
        )
        return token

    @classmethod
    def authenticate(cls, login, password):
        user = cls.query.filter(cls.login == login).one()
        if not bcrypt.verify(password, user.password):
            raise Exception('No user with this password')
        return user
