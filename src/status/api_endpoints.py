"""
"   Created by: Josh on 1/03/18
"""

from flask import Blueprint, jsonify, url_for

from status.access import MicroserviceAccess, Access
import config as CONFIG

blueprint = Blueprint('api_status', __name__, url_prefix='/status/api')
service_name = "API"


@blueprint.route('/actions')
def get_actions():
    actions = {
        'status': url_for('.check_api'),
        'local': url_for('.check_local'),
        'external': url_for('.check_external'),
        'domain': url_for('.check_domain'),
    }
    return jsonify(actions)


@blueprint.route('/')
def check_api():
    msg = dict()

    local_access = Access(ip=CONFIG.LOCAL_ADDRESS, port="5000", endpoint="/api")
    external_access = Access(ip=CONFIG.EXTERNAL_IP, port="80", endpoint="/api")
    domain_access = Access(ip=CONFIG.DOMAIN_NAME, endpoint="/api")

    api_service = MicroserviceAccess(service_name)

    msg[service_name] = api_service.check_all(local=local_access, external=external_access, domain=domain_access)
    return jsonify(msg), 200


@blueprint.route('/local')
def check_local():
    access = Access(ip=CONFIG.LOCAL_ADDRESS, port="5000", endpoint="/api")
    api_service = MicroserviceAccess(service_name)
    return jsonify({ "local": api_service.local(access) }), 200


@blueprint.route('/external')
def check_external():
    access = Access(ip=CONFIG.EXTERNAL_IP, port="80", endpoint="/api")
    api_service = MicroserviceAccess(service_name)
    return jsonify({"external": api_service.external(access)}), 200


@blueprint.route('/domain')
def check_domain():
    access = Access(ip=CONFIG.DOMAIN_NAME, endpoint="/api")
    api_service = MicroserviceAccess(service_name)
    return jsonify({"domain": api_service.domain(access)}), 200