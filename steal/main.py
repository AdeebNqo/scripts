import sys
import subprocess
import time
import pyinotify
import asyncore



#------------------------------------------------------
#Monitor change to folder which belongs to this process
#------------------------------------------------------

print('Now setting up folder listener...')

wm = pyinotify.WatchManager()
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE

class EventHandler(pyinotify.ProcessEvent):
	def process_IN_CREATE(self,event):
		print('created')
	def process_IN_DELETE(self, event):
		print('deleted')
	def process_default(self,event):
		print('something happed in folder')

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/tmp', mask, rec=True)
#wdd = wmanager.add_watch('/proc/'+str(lynda_pid)+'/fd/', actions, rec=True)
#print('watching /proc/'+str(lynda_pid)+'/fd/')
asyncore.loop()

#------------------------------------------------------

#------------------------------------------------------
def run_cmd(cmd):
	return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


storage_dir = sys.argv[1]

sys.stdout.write('Searching for lynda.com widget pid...')
#Getting process number of the flash player
result = run_cmd('lsof -n | grep Flash')
output = result.stdout.read().strip()
tokens = output.split()
if (len(tokens)>0):
	lynda_pid = int(tokens[1])
	sys.stdout.write('Done!\n')
	while(True):
		a =1
else:
	print('lynda not detected.')

