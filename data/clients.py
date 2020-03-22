import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Client(SqlAlchemyBase):
    __tablename__ = 'clients'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name_surname = sqlalchemy.Column(sqlalchemy.String)

    events = orm.relation("Event", back_populates='client')
