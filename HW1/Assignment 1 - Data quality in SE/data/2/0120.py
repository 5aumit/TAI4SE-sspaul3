def processInstruction(inst, idx, acc):
	opCode, value = inst.split()
	if opCode == 'nop':
		return idx + 1, acc;
	elif opCode == 'jmp':
		return idx + int(value), acc
	elif opCode == 'acc':
		return idx + 1, acc + int(value)

with open('Input') as inFile:
	lines = inFile.read().splitlines()

alreadyVisited = []
currentIndex = 0
acc = 0

while True:
	if currentIndex in alreadyVisited:
		print('Hit an already run instruction')
		break
	else:
		alreadyVisited.append(currentIndex)
	currentIndex, acc = processInstruction(lines[currentIndex], currentIndex, acc)

print('Part 1:', acc)

for changedIndex in range(len(lines)):
	tempInstructions = lines[:]
	if tempInstructions[changedIndex].startswith('acc'):
		continue
	elif tempInstructions[changedIndex].startswith('jmp'):
		tempInstructions[changedIndex] = tempInstructions[changedIndex].replace('jmp', 'nop')
	else:
		tempInstructions[changedIndex] = tempInstructions[changedIndex].replace('nop', 'jmp')
	
	alreadyVisited = []
	currentIndex = 0
	acc = 0
	while True:
		if currentIndex in alreadyVisited:
			break
		else:
			alreadyVisited.append(currentIndex)
		if currentIndex	== len(tempInstructions):
			print('Part 2:', acc)
			exit()
		currentIndex, acc = processInstruction(tempInstructions[currentIndex], currentIndex, acc)
