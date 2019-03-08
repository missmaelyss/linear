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

def scale(values):
	maxKm = max(values[0])

def estimatePrice(mileage, theta):
	return (theta[0]) + (theta[1] * mileage)

def IsThetaSame(theta, oldTheta):
	if abs((theta[0] + theta[1]) - (oldTheta[0] + oldTheta[1])) < 0.001:
		return 1
	return 0

def training(values, learningRate, theta):
	i = 0
	oldTheta = (-1, -1)
	while i < 200 and IsThetaSame(theta, oldTheta) == 0:
		doze = 0.0
		doze2 = 0.0
		for value in values:
			doze += estimatePrice(float(value[0]), theta) - float(value[1])
			doze2 += (estimatePrice(float(value[0]), theta) - float(value[1])) * float(value[0])
		oldTheta = theta
		theta = (theta[0] - (learningRate) * (1.0/(len(values))) * doze, theta[1] - (learningRate) * (1.0/(len(values))) * doze2)
		i += 1
	return (theta)

def main():
	values = readFile()

	print(values)
	# print(training(values, 0.1, (0,1)))
main()