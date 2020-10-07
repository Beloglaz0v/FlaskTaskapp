from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from config import Config
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from schemas import TaskSchema, UserSchema, AuthSchema
from flask_apispec import use_kwargs, marshal_with

app = Flask(__name__)
app.config.from_object(Config)

client = app.test_client()

engine = create_engine('sqlite:///db.sqlite')

session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

jwt = JWTManager(app)

docs = FlaskApiSpec()
docs.init_app(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='videoblog',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})


from models import *

Base.metadata.create_all(bind=engine)


@app.route('/tasks', methods=['GET'])
@jwt_required
@marshal_with(TaskSchema(many=True))
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter(Task.user_id == user_id)
    return tasks


@app.route('/new_task', methods=['POST'])
@jwt_required
@use_kwargs(TaskSchema)
@marshal_with(TaskSchema)
def new_tasks(**kwargs):
    user_id = get_jwt_identity()
    new_one = Task(user_id=user_id, **kwargs)
    session.add(new_one)
    session.commit()
    return new_one


@app.route('/update_task/<int:task_id>', methods=['PUT'])
@jwt_required
@use_kwargs(TaskSchema)
@marshal_with(TaskSchema)
def update_task(task_id, **kwargs):
    user_id = get_jwt_identity()
    item = Task.query.filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    for key, value in kwargs.items():
        setattr(item, key, value)
    session.commit()
    return item


@app.route('/delete_task/<int:task_id>', methods=['DELETE'])
@jwt_required
@marshal_with(TaskSchema)
def delete_task(task_id):
    user_id = get_jwt_identity()
    item = Task.query.filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    session.delete(item)
    session.commit()
    return '', 204


@app.route('/register', methods=['POST'])
@use_kwargs(UserSchema)
@marshal_with(AuthSchema)
def register(**kwargs):
    user = User(**kwargs)
    session.add(user)
    session.commit()
    token = user.get_token()
    return {'access_token': token}


@app.route('/login', methods=['POST'])
@use_kwargs(UserSchema(only=('login', 'password')))
@marshal_with(AuthSchema)
def login():
    params = request.json
    user = User.authenticate(**params)
    token = user.get_token()
    return {'access_token': token}


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == '__main__':
    app.run()
