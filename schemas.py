from marshmallow import Schema, validate, fields
import time


class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(dump_only=True)
    title = fields.String(required=True, validate=[
        validate.Length(max=250)])
    description = fields.String(required=False, validate=[
        validate.Length(max=500)])
    date = fields.DateTime(format='%d.%m.%Y %H:%M:%S', dump_only=True)
    status = fields.Integer(required=True)
    deadline = fields.Date(required=False)
    message = fields.String(dump_only=True)


class UserSchema(Schema):
    login = fields.String(required=True, validate=[
        validate.Length(max=100)])
    password = fields.String(required=True, validate=[
        validate.Length(max=100)], load_only=True)
    tasks = fields.Nested(TaskSchema, many=True, dump_only=True)


class AuthSchema(Schema):
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)
