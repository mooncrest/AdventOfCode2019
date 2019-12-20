def parseOpCode(inputCodes, part1=False):
	if part1:
		inputCodes[1] = 12
		inputCodes[2] = 2
	
	index = 0
	while True:
		if inputCodes[index] == 1:
			val1 = inputCodes[inputCodes[index + 1]]
			val2 = inputCodes[inputCodes[index + 2]]
			inputCodes[inputCodes[index + 3]] = val1 + val2
		
		elif inputCodes[index] == 2:
			val1 = inputCodes[inputCodes[index + 1]]
			val2 = inputCodes[inputCodes[index + 2]]
			inputCodes[inputCodes[index + 3]] = val1 * val2

		elif inputCodes[index] == 99:
			break;

		else:
			raise Exception("op code was not formatted correctlly")
	
		index += 4

def Part2BruteForce(inputCodes):
	for x in range(100):
		for y in range(100):
		
			valuesCopy = inputCodes[:]
			valuesCopy[1] = x
			valuesCopy[2] = y
			try:
				parseOpCode(valuesCopy)
				if valuesCopy[0] == 19690720:
					print(100 * x + y)
					break

			except Exception:
				pass
	

if __name__ == "__main__": 
	# parsing input
	file = open("input.txt")
	inputString = file.readline()
	values = [int(i) for i in inputString.split(",")]
	
	# execution begins
	
	# part1
	copy = values[:]
	parseOpCode(copy, True)	
	print(copy[0])
	
	# part2
	Part2BruteForce(values)
