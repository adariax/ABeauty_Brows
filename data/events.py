import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

import datetime


class Event(SqlAlchemyBase):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    client_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("clients.id"))
    client = orm.relation("Client")

    note = sqlalchemy.Column(sqlalchemy.TEXT)
    created_date = sqlalchemy.Column(sqlalchemy.Date, default=datetime.date)

    def get_items(self):
        return [self.created_date, self.note]
