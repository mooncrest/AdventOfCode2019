def calculateFuel(fuel): 
	return fuel // 3 - 2

if __name__ == "__main__": 
	file = open("input.txt")
	print(sum(calculateFuel(int(fuel)) for fuel in file))
