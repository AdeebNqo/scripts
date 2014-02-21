import sys
import subprocess
import time
import pyinotify
from pyinotify import *

def run_cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
storage_dir = sys.argv[1]
#print("Will wait for about 20 seconds in case first video hasn't started.")
#time.sleep(20)

sys.stdout.write('Searching for lynda.com widget pid...')
#Getting process number of the flash player
result = run_cmd('lsof -n | grep Flash')
output = result.stdout.read().strip()
tokens = output.split()
lynda_pid = int(tokens[1])
sys.stdout.write('Done!\n')
#------------------------------------------------------
#Monitor change to folder which belongs to this process
#------------------------------------------------------

print('Now setting up folder listener...')

class PClose(ProcessEvent):
        def process_IN_DELETE(self, event):
            print('deleted')

watchMonitor = pyinotify.WatchManager()
notifier = pyinotify.Notifier(watchMonitor)
watchMonitor.add_watch('/proc/'+str(lynda_pid)+'/fd', pyinotify.ALL_EVENTS)
notifier.loop()
