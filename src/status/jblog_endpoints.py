"""
"   Created by: Josh on 10/03/18
"""

from flask import Blueprint, jsonify, url_for

from status.access import MicroserviceAccess, Access
#from src.config import *
import config as CONFIG

blueprint = Blueprint('jblog_status', __name__, url_prefix='/status/jblog')
service_name = "JBlog"


@blueprint.route('/actions')
def get_actions():
    actions = {
        'status': url_for('.check_jblog'),
        'local': url_for('.check_local'),
        'external': url_for('.check_external'),
        'domain': url_for('.check_domain'),
    }
    return jsonify(actions)


@blueprint.route('/')
def check_jblog():
    msg = dict()

    local_access = Access(ip=CONFIG.LOCAL_ADDRESS, port="4000")
    external_access = Access(ip=CONFIG.EXTERNAL_IP, port="80", endpoint="/jblog")
    domain_access = Access(ip=CONFIG.DOMAIN_NAME, endpoint="/jblog")

    jblog_service = MicroserviceAccess(service_name)

    msg[service_name] = jblog_service.check_all(local=local_access, external=external_access, domain=domain_access)
    return jsonify(msg), 200


@blueprint.route('/local')
def check_local():
    access = Access(ip=CONFIG.LOCAL_ADDRESS, port="4000")
    jblog_service = MicroserviceAccess(service_name)
    return jsonify({ "local": jblog_service.local(access) }), 200


@blueprint.route('/external')
def check_external():
    access = Access(ip=CONFIG.EXTERNAL_IP, port="80", endpoint="/jblog")
    jblog_service = MicroserviceAccess(service_name)
    return jsonify({"external": jblog_service.external(access)}), 200


@blueprint.route('/domain')
def check_domain():
    access = Access(ip=CONFIG.DOMAIN_NAME, endpoint="/jblog")
    jblog_service = MicroserviceAccess(service_name)
    return jsonify({"domain": jblog_service.domain(access)}), 200