import subprocess
import tempfile
import shutil


from os.path import expanduser
home = expanduser("~")

term = "Flash"
cmd = "lsof -n | grep Flash"

ps_process = subprocess.Popen(["lsof", "-n"], stdout=subprocess.PIPE)

grep_process = subprocess.Popen(["grep", term], stdin=ps_process.stdout, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

ps_process.stdout.close() 

output = grep_process.communicate()[0]
#process id
pid = (output.split()[1])

filename = tempfile.NamedTemporaryFile().name
filename = filename.replace("/tmp","")
print("moving file...")
print("src: "+"/proc/"+pid+"/fd/15")
print("dest: "+home+"/Videos/"+filename)
shutil.copy("/proc/"+pid+"/fd/15", home+"/Videos/"+filename)
