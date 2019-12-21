def createHashMap(moves):
	positions = {}
	xCord = 0
	yCord = 0
	for move in moves:
		if move[0] == 'R':
			for i in range(int(move[1:])):
				xCord += 1
				positions.setdefault(xCord, {}).setdefault(yCord, True)

		elif move[0] == 'L':
			for i in range(int(move[1:])):
				xCord -= 1
				positions.setdefault(xCord, {}).setdefault(yCord, True)

		elif move[0] == 'D':
			for i in range(int(move[1:])):
				yCord -= 1
				positions.setdefault(xCord, {}).setdefault(yCord, True)

		elif move[0] == 'U':
			for i in range(int(move[1:])):
				yCord += 1
				positions.setdefault(xCord, {}).setdefault(yCord, True)

		else:
			raise Exception("op code does not exist")

	return positions

def findIntersections(moves, hashmap):
	xCord = 0
	yCord = 0
	manhattenDis = float('inf')

	box = float("inf")
	for move in moves:
		if move[0] == 'R':
			for i in range(int(move[1:])):
				xCord += 1
				if hashmap.get(xCord, {}).get(yCord, False) and abs(xCord) + abs(yCord) < manhattenDis:
					manhattenDis = abs(xCord) + abs(yCord)

		elif move[0] == 'L':
			for i in range(int(move[1:])):
				xCord -= 1
				if hashmap.get(xCord, {}).get(yCord, False) and abs(xCord) + abs(yCord) < manhattenDis:
					manhattenDis = abs(xCord) + abs(yCord)

		elif move[0] == 'D':
			for i in range(int(move[1:])):
				yCord -= 1
				if hashmap.get(xCord, {}).get(yCord, False) and abs(xCord) + abs(yCord) < manhattenDis:
					manhattenDis = abs(xCord) + abs(yCord)

		elif move[0] == 'U':
			for i in range(int(move[1:])):
				yCord += 1
				if hashmap.get(xCord, {}).get(yCord, False) and abs(xCord) + abs(yCord) < manhattenDis:
					manhattenDis = abs(xCord) + abs(yCord)

		else:
			raise Exception("op code does not exist")

	return manhattenDis


def createStepHashMap(moves):
	positions = {}
	xCord = 0
	yCord = 0
	steps = 0
	for move in moves:
		if move[0] == 'R':
			for i in range(int(move[1:])):
				steps += 1
				xCord += 1
				positions.setdefault(xCord, {}).setdefault(yCord, steps)

		elif move[0] == 'L':
			for i in range(int(move[1:])):
				steps += 1
				xCord -= 1
				positions.setdefault(xCord, {}).setdefault(yCord, steps)

		elif move[0] == 'D':
			for i in range(int(move[1:])):
				steps += 1
				yCord -= 1
				positions.setdefault(xCord, {}).setdefault(yCord, steps)

		elif move[0] == 'U':
			for i in range(int(move[1:])):
				steps += 1
				yCord += 1
				positions.setdefault(xCord, {}).setdefault(yCord, steps)

		else:
			raise Exception("op code does not exist")

	return positions

def findLowestStepIntersections(moves, hashmap):
	xCord = 0
	yCord = 0
	lowestSteps = float('inf')
	steps = 0
	for move in moves:
		if move[0] == 'R':
			for i in range(int(move[1:])):
				xCord += 1
				steps += 1
				stepCount = hashmap.get(xCord, {}).get(yCord, 0)
				if stepCount and stepCount + steps < lowestSteps:
					lowestSteps = stepCount + steps

		elif move[0] == 'L':
			for i in range(int(move[1:])):
				xCord -= 1
				steps += 1
				stepCount = hashmap.get(xCord, {}).get(yCord, 0)
				if stepCount and stepCount + steps < lowestSteps:
					lowestSteps = stepCount + steps


		elif move[0] == 'D':
			for i in range(int(move[1:])):
				yCord -= 1
				steps += 1
				stepCount = hashmap.get(xCord, {}).get(yCord, 0)
				if stepCount and stepCount + steps < lowestSteps:
					lowestSteps = stepCount + steps


		elif move[0] == 'U':
			for i in range(int(move[1:])):
				yCord += 1
				steps += 1
				stepCount = hashmap.get(xCord, {}).get(yCord, 0)
				if stepCount and stepCount + steps < lowestSteps:
					lowestSteps = stepCount + steps


		else:
			raise Exception("op code does not exist")

	return lowestSteps


if __name__ == "__main__":
	file = open("input.txt")
	move1 = file.readline().strip().split(",")
	move2 = file.readline().strip().split(",")

	# move1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
	# move2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")

	# move1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
	# move2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")

	# move1 = "R8,U5,L5,D3".split(",")
	# move2 = "U7,R6,D4,L4".split(",")
	# print(createHashMap(move1))

	# part1
	print(findIntersections(move2, createHashMap(move1)))


	# part2
	print(findLowestStepIntersections(move2, createStepHashMap(move1)))