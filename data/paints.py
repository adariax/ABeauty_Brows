import sqlalchemy
from .db_session import SqlAlchemyBase


class Paint(SqlAlchemyBase):
    __tablename__ = 'paints'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    title = sqlalchemy.Column(sqlalchemy.String)
