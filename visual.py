import sys
import json
import matplotlib.pyplot as plt

def estimatePrice(mileage, theta):
	return (theta[0]) + (theta[1] * mileage)

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
				km.append(float(line[0]))
				price.append(float(line[1]))
			lenLine = len(line)
		return km, price

def main():
	try:
		file = open('coef.py', "r")
	except:
		print('No coef file')
		theta0 = 0
		theta1 = 0
	else:
		js = file.read()
		coef = json.loads(js)
		theta0 = coef["t0"]
		theta1 = coef["t1"]

	km, price = readFile()

	plt.scatter(km, price,c = 'navy',marker = '+', edgecolors = 'none')
	if theta0 != 0 and theta1 != 0:
		plt.plot([min(km), max(km)], [estimatePrice(min(km), (theta0, theta1)), estimatePrice(max(km), (theta0, theta1))], color = 'red', linestyle = 'solid')
	plt.title('graph')
	plt.show()

main()
