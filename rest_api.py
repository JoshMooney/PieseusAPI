import sys
import os.path

from flask import Flask
import optparse
import config as CONFIG

# Status endpoints
from status.endpoints import blueprint as status_blueprint
from status.jblog_endpoints import blueprint as jblog_status_blueprint
from status.resume_endpoints import blueprint as resume_status_blueprint
from status.api_endpoints import blueprint as api_status_blueprint

from webscrapper.endpoints import blueprint as scrapper_blueprint

def create_app(config='config'):
    app = Flask(__name__)
    app.config.from_object(config)

    # Add blueprints to site here
    app.register_blueprint(status_blueprint)
    app.register_blueprint(jblog_status_blueprint)
    app.register_blueprint(resume_status_blueprint)
    app.register_blueprint(api_status_blueprint)

    app.register_blueprint(scrapper_blueprint)

    return app

def init_flags():
    parser = optparse.OptionParser()

    parser.add_option("-H", "--host", help="Hostname of the Flask app [default %s]" % CONFIG.LOCAL_ADDRESS, default=CONFIG.LOCAL_ADDRESS)
    parser.add_option("-P", "--port", help="Port of the Flask app [default %s]" % CONFIG.DEFAULT_PORT, default=CONFIG.DEFAULT_PORT)

    return parser.parse_args()

app = create_app()
options, args = init_flags()

if __name__ == '__main__':
    app.run(threaded=True, host=options.host, port=int(options.port))
