
#sum of all integers that are multiples of 3 and/or 5 under a variable number


num1 = int(input("Enter Your Number!"))
array1 = []

		for i in range(0, num1):
			if i%3 == 0:
				array1.append(int(i))
			elif i%5 == 0: 
				array1.append(int(i))


		num2 = sum(array1)

		print("The sum of all integers that are multiples of 3 and/or 5 under YOUR number is", num2)


