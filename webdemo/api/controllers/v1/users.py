

import pecan
from pecan import rest
from wsme import types as wtypes

from webdemo.api import expose


class User(wtypes.Base):
    id = wtypes.text
    name = wtypes.text
    age = int


class Users(wtypes.Base):
    users = [User]


class UserController(rest.RestController):

    def __init__(self, user_id):
        self.user_id = user_id

    @expose.expose(User)
    def get(self):
        user_info = {
            'id': self.user_id,
            'name': 'Alice',
            'age': 30,
        }
        return User(**user_info)

    @expose.expose(User, body=User)
    def put(self, user):
        user_info = {
            'id': self.user_id,
            'name': user.name,
            'age': user.age + 1,
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
        user_info_list = [
            {
                'name': 'Alice',
                'age': 30,
            },
            {
                'name': 'Bob',
                'age': 40,
            }
        ]
        users_list = [User(**user_info) for user_info in user_info_list]
        return Users(users=users_list)

    @expose.expose(None, body=User, status_code=201)
    def post(self, user):
        print user
