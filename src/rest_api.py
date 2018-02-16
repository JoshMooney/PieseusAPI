import sys
import os.path

from flask import Flask
import optparse

from status.server_status import blueprint as status_blueprint

default_host = '127.0.0.1'
default_port = '5000'

def create_app(config='config'):
    app = Flask(__name__)
    app.config.from_object(config)

    # Add blueprints to site here
    app.register_blueprint(status_blueprint)

    return app

app = create_app()

parser = optparse.OptionParser()

parser.add_option("-H", "--host", help="Hostname of the Flask app [default %s]" % default_host, default=default_host)
parser.add_option("-P", "--port", help="Port of the Flask app [default %s]" % default_port, default=default_port)

options, _ = parser.parse_args()

if __name__ == '__main__':
    app.run(threaded=True, host=options.host, port=int(options.port))
