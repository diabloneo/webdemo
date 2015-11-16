
from pecan import rest
from wsme import types as wtypes

from webdemo.api.controllers.v1 import users as v1_users
from webdemo.api import expose


class V1Controller(rest.RestController):
    users = v1_users.UsersController()

    @expose.expose(wtypes.text)
    def get(self):
        return 'webdemo v1controller'
