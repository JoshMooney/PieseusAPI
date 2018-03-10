import os



# Navigate to The correct directory
theseus_jblog_dir = '/home/pi/Project/JBlog'
os.chdir(theseus_jblog_dir)

def git_status(self):
    print
    "Checking Git Status of JBlog"
    theseus_jblog_dir = '/home/pi/Project/PieseusResume'
    os.chdir(theseus_jblog_dir)
    subprocess.check_output("git fetch", shell=True)
    status = subprocess.check_output("git status", shell=True)
    git_msg = 'Resume is ' + colored('behind', 'red') + ' by '
    if ("up-to-date" in status):
        git_msg = 'Resume is branch origin/master ' + colored('up-to-date', 'green')
        print(git_msg)
    else:
        start = status.find('by', 0, len(status))
        end = status.find(',', 0, len(status))
        behind_msg = status[start: end]
        print(git_msg + behind_msg)

# Get server uptime
print('')
print('-- Server Uptime --')
try:
    status = subprocess.check_output("uptime", shell=True)
    start = status.find('up', 0, len(status))
    end = status.find(',', 0, len(status))
    up_time = status[start: end]
    comp_name = platform.node()
    print(comp_name + " server has been " + up_time)
except Exception, err:
    print
    err