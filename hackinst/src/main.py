import os
import subprocess
import sys
import shutil
def copy(File, destdir):
	shutil.copy(File, destdir)
def run_cmd(cmd):
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	return proc.stdout.readlines()
def main():
	filename = sys.argv[1]
	f = open(filename)
	lines = f.readlines()
	for line in lines:
		words = line.split()
		package = words[1]
		try:
			print('Copying '+package)
			os.mkdir(package)
			#Locating all subfiles of package
			f = open(package+'/list.txt','wb')
			files = run_cmd('locate '+package)
			for File in files:
				f.write(File)
				File = File.replace('\n','')
				copy(File, package)	
		except Exception as err:
			print('Could not process '+package+' fully.')
			print(err)
if __name__=='__main__':
	main()
