
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fib1 = []

num1 = 1
num2 = 1

upper_bound = int(input("Upperbound  "))

f= 0

while True:
	f = num1 + num2
	if f >= upper_bound:
		break

	elif	f%2 == 0:
		fib1.append(int(f))
		f2 = f
		num1 = num2
		num2 = f2
	else:
		f2 = f
		num1 = num2
		num2 = f2

ans=sum(fib1)
print("The sum of the even-valued fibonacci series terms smaller than upperbound is", ans)
