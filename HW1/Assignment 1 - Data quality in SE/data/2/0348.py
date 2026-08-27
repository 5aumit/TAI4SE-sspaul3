"""Scans all files in this project for FIXME and TODO comments and writes them to todos.txt
has to be invoked while being in myLambda/ and not in e.g. myLambda/src"""
import sys
import os
import re
files = []
searchFiles = []

# get all subdirs and its files
for root, dirs, f in os.walk('./'):
	files.append((root, f))

# build filepaths out of dir and filename
for f in files[0][1]:
	searchFiles.append(files[0][0] + str(f))	# we're in ./ so we can just concat directory's name with filename

for i in range(1,len(files)):	# we're in subdirs so we have to add '/' to get real paths
	for f in files[i][1]:
		searchFiles.append(files[i][0] + '/'+ f)
files = searchFiles

#remove unwanted files
blacklist = ['./todos.txt', './todoGen.py'] + \
		[f for f in files if '__' in f or f[-3:] =='pyc' or '.git' in f]
for b in blacklist:
	files.remove(b)

print 'searching:'
map(lambda x: sys.stdout.write(x + '\n'), files)

TODO = re.compile('TODO.*')	# everything after TODO in one line
FIXME = re.compile('FIXME.*') # everything after FIXME in one line

# gather todos and fixmes
todos = []
fixmes = []
for f in files:
	with open(f) as fi:
		lineNumber = 0
		for line in fi:
			lineNumber +=1
			todo = re.search(TODO, line)
			fixme = re.search(FIXME, line)
			if todo:
				todos.append((todo.group(0), f, lineNumber))
			elif fixme:
				fixmes.append((fixme.group(0), f, lineNumber))


f = open('todos.txt', 'w')		#write fixmes and todos to todos.txt

f.write('#TODO#\n')

if todos == []:
	f.write('All todos are done')
else:
	for i in range(len(todos)):
		f.write('\t' + todos[i][0] + ' in file ' + todos[i][1] + ' in line ' + str(todos[i][2]) + '\n')

f.write('#FIXME#\n')

if fixmes == []:
	f.write('Nothing to fix')
else:
	for i in range(len(fixmes)):
		f.write('\t'+ fixmes[i][0] + ' in file ' + fixmes[i][1] + ' in line ' + str(fixmes[i][2]) + '\n')

print "Done"
