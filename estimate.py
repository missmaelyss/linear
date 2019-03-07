def estimatePrice(mileage, theta0, theta1):
	return (theta0) + (theta1 * mileage)

def main():
	global theta0
	global theta1
	theta0 = 0
	theta1 = 0
	mileage = input('Enter a mileage:\t')
	try:
		mileage = int(mileage)
	except:
		print('Error:\tNot a number')
		main()
	else:
		print('EstimatePrice:\t', estimatePrice(mileage, theta0, theta1))
main()
