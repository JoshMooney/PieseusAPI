import sys
import os.path

from flask import Flask
import optparse

from status.endpoints import blueprint as status_blueprint

default_host = '127.0.0.1'
default_port = '5000'

def create_app(config='config'):
    app = Flask(__name__)
    app.config.from_object(config)

    # Add blueprints to site here
    app.register_blueprint(status_blueprint)

    return app

def init_flags():
    parser = optparse.OptionParser()

    parser.add_option("-H", "--host", help="Hostname of the Flask app [default %s]" % default_host, default=default_host)
    parser.add_option("-P", "--port", help="Port of the Flask app [default %s]" % default_port, default=default_port)

    return parser.parse_args()

app = create_app()
options, args = init_flags()

if __name__ == '__main__':
    app.run(threaded=True, host=options.host, port=int(options.port))
