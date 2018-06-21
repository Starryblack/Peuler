#What is the largest prime factor of the number?


x= int(input("Number?   "))
lol=x
q=x


for y in range(2, (x//2)+1):

	if y <= q:
		temp=0
		while q%y==0:
			q=q/y
			temp=temp+1
	
		if temp > 0:
			lol=y
			print(lol)
		
	else:
		break
print(lol)



	
	
