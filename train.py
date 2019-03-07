import sys

def readFile():
	args = []
	min = None
	max = None
	for arg in sys.argv[1:]:
		args.append(arg)
	try:
		file = open(args[0], "r")
		file = file.read()
		file = file.split('\n')
		if file[len(file) - 1] == '' :
			del file[len(file) - 1]
	except IndexError as e:
		print('Error:\tNo file')
		exit()
	except FileNotFoundError as e:
		print('Error:\t', e)
		exit()
	except PermissionError as e:
		print('Error:\t', e)
	except:
		print('Error')
		exit()
	else:
		values = []
		lenLine = -1
		for line in file:
			line = line.split(',')
			if len(line) != lenLine and lenLine != -1:
				print('Error:\tNot good file')
				exit()
			if lenLine == -1:
				pass
			else:
				values.append((int(line[0]), int(line[1])))
				if (min is None or int(line[0]) < min):
					min = int(line[0])
				if (max is None or int(line[0]) > max):
					max = int(line[0])
			lenLine = len(line)
		return (values, min, max)

def estimatePrice(mileage, theta):
	return (theta[0]) + (theta[1] * mileage)

def training(values, learningRate, theta, max, min):
	theta0 = theta[0]
	theta1 = theta[1]
	div = float(max - min)
	if (div == 0):
		div = float(1)
	i = 1
	while i < learningRate:
		doze = 0
		doze2 = 0
		for value in values:
			doze += estimatePrice(((value[0] - min) / div), (theta0, theta1)) - value[1]
			doze2 += (estimatePrice(((value[0] - min) / div), (theta0, theta1)) - value[1]) * ((value[0] - min) / div)
		theta0 -= (1.0 / i) * (1.0/(len(values))) * doze
		theta1 -= (1.0 / i) * (1.0/(len(values))) * doze2
		i += 1
	print((theta0 + (theta1 * ((42000 - min) / div))))
	return (theta0,theta1)

def main():
	min = 0
	max = 0
	values, min, max = readFile()
	print(training(values, 10000, (0,0), max, min))
main()