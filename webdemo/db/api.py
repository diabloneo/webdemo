
from sqlalchemy import create_engine
import sqlalchemy.orm
from sqlalchemy.orm import exc

from webdemo.db import models as db_models


_ENGINE = None
_SESSION_MAKER = None


def get_engine():
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE

    _ENGINE = create_engine('sqlite:///webdemo.db')
    return _ENGINE


def get_session_maker(engine):
    global _SESSION_MAKER
    if _SESSION_MAKER is not None:
        return _SESSION_MAKER

    _SESSION_MAKER = sqlalchemy.orm.sessionmaker(bind=engine)
    return _SESSION_MAKER


def get_session():
    engine = get_engine()
    maker = get_session_maker(engine)
    session = maker()

    return session


class Connection(object):

    def __init__(self):
        pass

    def get_user(self, user_id):
        query = get_session().query(db_models.User).filter_by(user_id=user_id)
        try:
            user = query.one()
        except exc.NoResultFound:
            # TODO(developer): process this situation
            pass

        return user

    def list_users(self):
        session = get_session()
        query = session.query(db_models.User)
        users = query.all()

        return users

    def update_user(self, user):
        pass

    def delete_user(self, user):
        pass
