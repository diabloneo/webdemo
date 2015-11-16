
import pecan

from webdemo.api import config as api_config


def get_pecan_config():
    filename = api_config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)


def setup_app():
    config = get_pecan_config()

    app_conf = dict(config.app)
    app = pecan.make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        **app_conf
    )

    return app
