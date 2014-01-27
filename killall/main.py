import subprocess

f = open("output.txt")
lines = f.readlines()
for line in lines:
	pid = line.split()[0]
	print(pid)
	subprocess.Popen("kill -9 "+pid,shell=True);
