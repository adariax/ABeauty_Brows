import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Paint(SqlAlchemyBase):
    __tablename__ = 'paints'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String)

    events = orm.relation("Event", back_populates='paint')
