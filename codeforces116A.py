n = int(raw_input())
capicity = 0
people = 0
for i in range(n):
	a,b = map(int,raw_input().split())
	people = people-a+b
	capicity = max(capicity,people)
print capicity