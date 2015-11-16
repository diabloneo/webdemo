

from pecan import rest
from wsme import types as wtypes

from webdemo.api import expose


class User(wtypes.Base):
    name = wtypes.text
    age = int


class Users(wtypes.Base):
    users = [User]


class UsersController(rest.RestController):

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
