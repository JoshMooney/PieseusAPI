"""
"   Created by: Josh on 16/02/18
"""

from flask import Blueprint, jsonify, current_app, request, Response, stream_with_context

blueprint = Blueprint('test', __name__, url_prefix='/test')


@blueprint.route('/')
def test():
    return 'Hello World!'