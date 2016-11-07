def Staircase(n):
	for i in range(1,n+1):
		print " "*(n-i) + "#"*i
		
n = int(raw_input())
Staircase(n)