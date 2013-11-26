import os
def get_name(path):
	terms = path.split('/')
	return terms[len(terms)-1]
def install(files, dirs):
	for Dir in dirs:
		if (Dir!='list.txt'):
			tmpDir = get_name(Dir).replace('\n','')
			for File in files:
				if (tmpDir==File):
					copy(File, Dir.replace(File,''))
def process(path):
	try:
		f = open(path+'/list.txt')
		lines = f.readlines()
		for filenames in os.walk(path):
			files = filenames[2]
			if (files==1):
				#create directories
				for line in lines:
					os.mkdir(line.replace('\n',''))
			else:
				install(files,lines)
	except Exception as err:
		print(err)
def main():
	path = '/home/adeeb/Documents/programming/hackinst/src'
	for dirpath,dirnames,filenames in os.walk(path):
		process(dirpath)
if __name__=='__main__':
	main()
