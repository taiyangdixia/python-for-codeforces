import math
n = int(raw_input())
i=1
queue = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
if n < 6 :
	print queue[n-1]
else :	
	while 5*(math.pow(2,i)-1) < n:
		i+=1
	k = n - 5*(math.pow(2,i-1)-1)
	pos = int(math.ceil(k/(math.pow(2,i-1))))
	print queue[pos-1]