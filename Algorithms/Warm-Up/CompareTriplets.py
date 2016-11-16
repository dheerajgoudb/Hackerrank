A = [int(i) for i in raw_input().split()]
B = [int(i) for i in raw_input().split()]
#print A,B
a,b = 0,0
for i in range(len(A)):
	if A[i] > B[i]:
		a += 1
	elif A[i] < B[i]:
		b += 1
	else:
		continue
print a,b
