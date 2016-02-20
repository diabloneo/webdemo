
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext import declarative
from sqlalchemy import Index


Base = declarative.declarative_base()


class User(Base):
    """User table"""

    __tablename__ = 'user'
    __table_args__ = (
        Index('ix_user_user_id', 'user_id'),
    )
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255), nullable=False)
    name = Column(String(64), nullable=False, unique=True)
    email = Column(String(255))
