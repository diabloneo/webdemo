
from pecan import rest
from wsme import types as wtypes

from webdemo.api import expose


class RootController(rest.RestController):

    @expose.expose(wtypes.text)
    def get(self):
        return "webdemo"
