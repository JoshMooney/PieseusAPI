"""
"   Created by: Josh on 16/03/18
"""

import os
import subprocess

# Global Varibles
PROJECT_DIR = "/home/pi/Project"
LOG_DIR = "/home/pi/_logs"
LOG_FILE_NAME = "log.%s.txt"
NOHUP_CMD = "nohup %s &"
PYTHON_CMD = "python %s > %s"

# Construct API start command
API = "PiesuesAPI"
api_dir = os.path.join(PROJECT_DIR, API)
log_dir = os.path.join(LOG_DIR, LOG_FILE_NAME % ('api'))
python_cmd = PYTHON_CMD % ('rest_api.py', log_dir)
api_cmd = NOHUP_CMD % (python_cmd)

# Execute API start command
cwd = os.getcwd()
os.chdir(api_dir)
print('Starting API')
status = subprocess.check_output(api_cmd, shell=True)
os.chdir(cwd)