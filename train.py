import sys
import copy

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
		km = []
		price = []
		lenLine = -1
		maxKm = -1
		for line in file:
			line = line.split(',')
			if len(line) != lenLine and lenLine != -1:
				print('Error:\tNot good file')
				exit()
			if lenLine == -1:
				pass
			else:
				if maxKm != -1:
					maxKm = max(float(line[0]), abs(float(line[0])), maxKm)
					maxPrice = max(float(line[1]), abs(float(line[1])), maxPrice)
				else:
					maxKm = max(float(line[0]), abs(float(line[0])))
					maxPrice = max(float(line[1]), abs(float(line[1])))
				km.append(float(line[0]))
				price.append(float(line[1]))
			lenLine = len(line)
		return km, price, maxKm, maxPrice

def scale(km, price, maxKm, maxPrice):
	i = 0
	newKm = copy.copy(km)
	newPrice = copy.copy(price)
	while i < len(km):
		newKm[i] = km[i] / maxKm
		newPrice[i] = price[i] / maxPrice
		i += 1
	return newKm, newPrice

def estimatePrice(mileage, theta):
	return (theta[0]) + (theta[1] * mileage)

def IsThetaSame(theta, oldTheta):
	if abs((theta[0] + theta[1]) - (oldTheta[0] + oldTheta[1])) < 0.0001:
		return 1
	return 0

def training(km, price, learningRate, theta):
	i = 0
	oldTheta = (-1, -1)
	while i < 200 and IsThetaSame(theta, oldTheta) == 0:
		doze = 0.0
		doze2 = 0.0
		n = 0
		while n < len(km):
			doze += estimatePrice(float(km[n]), theta) - float(price[n])
			doze2 += (estimatePrice(float(km[n]), theta) - float(price[n])) * float(km[n])
			n += 1
		oldTheta = theta
		theta = (theta[0] - (learningRate) * (1.0/(len(km))) * doze, theta[1] - (learningRate) * (1.0/(len(km))) * doze2)
		i += 1
	return (theta)

def main():
	km, price, maxKm, maxPrice = readFile()
	newKm, newPrice = scale(km, price, maxKm, maxPrice)
	theta = training(newKm, newPrice, 0.1, (0,1))
	file = open('coef.py', 'w')
	file.write('{ "t0":' + str(theta[0]) + ', "t1":' + str(theta[1]) + '}')

main()