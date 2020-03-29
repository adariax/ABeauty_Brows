import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

import datetime


class Event(SqlAlchemyBase):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    client_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("clients.id"))
    client = orm.relation("Client")

    paint_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("paints.id"))
    paint = orm.relation("Paint")

    note = sqlalchemy.Column(sqlalchemy.TEXT)
    created_date = sqlalchemy.Column(sqlalchemy.Date)
