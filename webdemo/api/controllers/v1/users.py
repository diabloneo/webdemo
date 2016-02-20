

import pecan
from pecan import request
from pecan import rest
from wsme import types as wtypes

from webdemo.api import expose


class User(wtypes.Base):
    id = int
    user_id = wtypes.text
    name = wtypes.text
    email = wtypes.text


class Users(wtypes.Base):
    users = [User]


class UserController(rest.RestController):

    def __init__(self, user_id):
        self.user_id = int(user_id)

    @expose.expose(User)
    def get(self):
        user_info = {
            'id': self.user_id,
            'name': 'Alice',
        }
        return User(**user_info)

    @expose.expose(User, body=User)
    def put(self, user):
        user_info = {
            'id': self.user_id,
            'name': user.name,
        }
        return User(**user_info)

    @expose.expose()
    def delete(self):
        print 'Delete user_id: %s' % self.user_id


class UsersController(rest.RestController):

    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder

    @expose.expose(Users)
    def get(self):
        db_conn = request.db_conn
        users = db_conn.list_users()
        users_list = []
        for user in users:
            u = User()
            u.id = user.id
            u.user_id = user.user_id
            u.name = user.name
            u.email = user.email
            users_list.append(u)
        return Users(users=users_list)

    @expose.expose(None, body=User, status_code=201)
    def post(self, user):
        print user
