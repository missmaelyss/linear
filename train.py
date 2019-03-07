import sys

def readFile():
	args = []
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
			lenLine = len(line)
		return values

def estimatePrice(mileage, theta):
	return (theta[0]) + (theta[1] * mileage)

def training(values, learningRate, theta):
	theta0 = theta[0]
	theta1 = theta[1]
	i = 0
	while i < 1:
		doze = 0
		doze2 = 0
		for value in values:
			doze += estimatePrice(value[0], (theta0, theta1)) - value[1]
			doze2 += (estimatePrice(value[0], (theta0, theta1)) - value[1]) * value[0]
		theta0 = (1.0 / learningRate) * (1.0/(len(values))) * doze
		theta1 = (1.0 / learningRate) * (1.0/(len(values))) * doze2
		i += 1
	return (theta0,theta1)

def main():
	values = readFile()
	print(training(values, 0.001, (0,0)))
main()