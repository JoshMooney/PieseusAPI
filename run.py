"""
"   Created by: Josh on 16/03/18
"""

import os
import subprocess

# start api
PROJECT_DIR = "/home/pi/Project"
API = "PiesuesAPI"
api_dir = os.path.join([PROJECT_DIR, API])

os.chdir(api_dir)
print('Starting API')
status = subprocess.check_output("nohup python rest_api.py &", shell=True)