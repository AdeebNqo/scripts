import sys
import subprocess
import time
import pyinotify

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
#Method for handling events on folder
def onFolderEvent(event):
	print('event detected!')
	print(dir(event))
watchMonitor = pyinotify.WatchManager()
notifier = pyinotify.Notifier(watchMonitor)
watchMonitor.add_watch('/proc/'+str(lynda_pid)+'/fd', pyinotify.ALL_EVENTS, proc_fun=onFolderEvent)
notifier.loop()
