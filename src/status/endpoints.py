"""
"   Created by: Josh on 10/03/18
"""

from flask import Blueprint, jsonify, current_app, request, Response, stream_with_context, url_for
from src.status.server_status import *

blueprint = Blueprint('server_status', __name__, url_prefix='/status')


@blueprint.route('/')
def status():
    return jsonify({ "api": api() }), 200


@blueprint.route('/actions')
def get_actions():
    actions = {
        'mounted-drives': url_for('.check_mounted_drives'),
        'teamviewer': url_for('.check_teamviewer'),
        'api': url_for('.status'),
        'vnc-server': url_for('.check_vnc_server'),
        'server': url_for('.check_server'),
        'uptime': url_for('.check_uptime'),
        'nginx': url_for('.check_nginx'),
        'samba': url_for('.check_samba'),
        'transmission-daemon': url_for('.check_transmission'),
    }
    return jsonify(actions)

@blueprint.route('/server')
def check_server():
    msg = dict()
    msg['mounted-drives'] = mounted_drives()
    msg['teamviewer'] = teamviewer()
    msg['api'] = api()
    msg['vnc-server'] = vnc_server()
    msg['uptime'] = uptime()
    msg['nginx'] = nginx()
    msg['samba'] = samba()
    msg['transmission-daemon'] = transmission()
    return jsonify(msg), 200


@blueprint.route('/mounted-drives')
def check_mounted_drives():
    return jsonify({ "mounted-drives": mounted_drives() }), 200


@blueprint.route('/teamviewer')
def check_teamviewer():
    return jsonify({ "teamviewer": teamviewer() }), 200


@blueprint.route('/vnc-server')
def check_vnc_server():
    return jsonify({ "vnc-server": vnc_server() }), 200


@blueprint.route('/uptime')
def check_uptime():
    return jsonify({ "uptime": uptime() }), 200


@blueprint.route('/nginx')
def check_nginx():
    return jsonify({ "nginx": nginx() }), 200


@blueprint.route('/samba')
def check_samba():
    return jsonify({ "samba": samba() }), 200


@blueprint.route('/transmission')
def check_transmission():
    return jsonify({ "transmission-daemon": transmission() }), 200