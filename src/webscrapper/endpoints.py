"""
"   Created by: Josh on 07/10/18
"""
import os
import config as CONFIG
from flask import Blueprint, jsonify, current_app, request, Response, stream_with_context, url_for
from webscrapper.flash import FlashScaper

blueprint = Blueprint('scrapper', __name__, url_prefix='/scrape')


@blueprint.route('/actions')
def get_actions():
    actions = {
        'flash': url_for('.scrape_flash'),
    }
    return jsonify(actions)

@blueprint.route('/flash')
def scrape_flash():
    scraper = FlashScaper(download_dir=CONFIG.FLASH_DOWNLOAD_DIR)
    results = scraper.download()
    return jsonify(results), 200
