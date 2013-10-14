n = int(raw_input())
output = 0
for i in range(n):
	p,v,t = map(int,raw_input().split())
	output += (p+v+t)/2
	
print output
	