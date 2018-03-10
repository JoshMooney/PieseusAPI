"""
"   Created by: Josh on 10/03/18
"""
import os
import subprocess
import platform

PASS = 200
ERROR = 400

def api():
    from src.rest_api import options
    return {
        "name": "API",
        "status": "True",
        'msg': "API is running on " + platform.node() + ", accessible via " + options.host + ":" + options.port,
        "value": options.host + ":" + options.port
    }


def mounted_drives():
    drives = [{"name": "ShortTerm", "path": "/media/pi/ShortTerm"},
              {"name": "Aegon", "path": "/mnt/Aegon"}]

    for d in drives:
        d['status'] = False
        d['msg'] = d['name'] + ' is not accessible via ' + d['path'] + "."
        if os.path.ismount(d['path']):
            d['status'] = True
            d['msg'] = d['name'] + ' can be accessed via ' + d['path'] + "."
    return drives


def teamviewer():
    log_msg = {'name': 'TeamViewer', 'msg': 'Teamviewer is not running on ' + platform.node() + "." }
    log_msg['status'] = False
    try:
        status = subprocess.check_output("ps aux | grep teamviewer", shell=True)
        if('/opt/teamviewer/tv_bin/TeamViewer'in status):
            log_msg['status'] = str(True)
            log_msg['msg'] = 'Teamviewer is running on ' + platform.node()
    except Exception as err:
        print(err)
    return log_msg


def vnc_server():
    log_msg = { 'name': 'VNC Server', "msg": "VNC Server is not running on " + platform.node() + "." }
    log_msg['status'] = False
    try:
        status = subprocess.check_output("ps -e | grep vnc", shell=True)
        if('Xtightvnc'in status):
            log_msg['status'] = True
            log_msg['msg'] = "VNC Server is running on " + platform.node()
    except Exception as err:
        print(err)
    return log_msg


def uptime():
    msg = { "name": "Server Uptime", "status": "False", "msg": "Failed to get uptime on " + platform.node() + ".", "value": "" }
    try:
        status = subprocess.check_output("uptime", shell=True)
        start = status.find('up', 0, len(status))
        end = status.find(',', 0, len(status))
        up_time = status[start: end]
        comp_name = platform.node()
        msg['status'] = 'True'
        msg['value'] = up_time
        msg['msg'] = comp_name + " server has been " + up_time
        print(comp_name + " server has been " + up_time)
    except Exception as err:
        print(err)
    return msg


def check_service(ser_name, ser_data):
    msg = {"name": ser_data['name'], "status": "False", "msg": ser_data['msg'] + "not running on " + platform.node() + "." }
    try:
        status = subprocess.check_output("service "+ ser_name +" status", shell=True)
        if ("Active: active (running)" in status):
            msg['status'] = "True"
            msg['msg'] = ser_data['msg'] + "running."
    except Exception as err:
        print(err)
    return msg


def nginx():
    return check_service('nginx', {'name': 'NGINX', 'msg': 'Nginx service is '})


def samba():
    return check_service('smbd', {'name': 'SAMBA', 'msg': 'Samba server is '})


def transmission():
    return check_service('transmission-daemon', {'name': 'TRANSMISSION', 'msg': 'Transmission-daemon is '})