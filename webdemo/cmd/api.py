
from wsgiref import simple_server

from webdemo.api import app


def main():
    host = '0.0.0.0'
    port = 8080

    application = app.setup_app()
    srv = simple_server.make_server(host, port, application)

    srv.serve_forever()


if __name__ == '__main__':
    main()
