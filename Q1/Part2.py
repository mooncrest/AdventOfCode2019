def calculateFuel(mass): 
	fuel = mass // 3 - 2
	return 0 if fuel < 0 else fuel + calculateFuel(fuel)

if __name__ == "__main__":
	file = open("input.txt")
	print(sum(calculateFuel(int(mass)) for mass in file))

