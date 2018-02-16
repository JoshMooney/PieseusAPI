"""
"   Created by: Josh on 16/02/18
"""
import subprocess
import re
import StringIO
import sys
from threading  import Thread


class TemplateNotFoundException(Exception):
    def __init__(self, msg):
        self.msg = msg


def run_command(cmd, cwd=None):
    process = subprocess.Popen(cmd,
                               cwd=cwd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    threads = []
    stdout = StringIO.StringIO()
    stderr = StringIO.StringIO()
    threads.append(tee(process.stdout, stdout, sys.stdout))
    threads.append(tee(process.stderr, stderr, sys.stderr))
    for t in threads: t.join() # wait for IO completion
    exit_code = process.wait()
    rv = {
        'stdout': strip_color_codes(stdout.getvalue()),
        'stderr': strip_color_codes(stderr.getvalue()),
        'exit_code': exit_code,
    }
    return rv