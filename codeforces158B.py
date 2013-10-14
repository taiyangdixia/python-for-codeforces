import math
n = int(raw_input())
a = raw_input().split()
taxi_num = a.count('4')
three = a.count('3')
two = a.count('2')
one = a.count('1')

three_plus_one = min(three,one)
three -= three_plus_one
one -= three_plus_one
taxi_num += three_plus_one

if three :
	taxi_num += three
if two%2 :
	taxi_num += math.ceil(two/2.0)
	one -= 2	
else :
	taxi_num += two/2	
if one :
	taxi_num +=math.ceil(one/4.0)
	
print int(taxi_num)
	
 