import json

def estimatePrice(mileage, theta0, theta1):
	return (theta0) + (theta1 * mileage)

def main():
	try:
		file = open('coef.py', "r")
	except:
		theta0 = 0
		theta1 = 0
	else:
		js = file.read()
		coef = json.loads(js)
		theta0 = coef["t0"]
		theta1 = coef["t1"]

	mileage = input('Enter a mileage:\t')
	try:
		mileage = int(mileage)
	except:
		print('Error:\tNot a number')
		main()
	else:
		print('Estimated Price:\t',estimatePrice(mileage, theta0, theta1))

main()
