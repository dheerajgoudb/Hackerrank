N = int(raw_input)
integers = [int(i) for i in raw_input().split()]
if len(integers) == N:
	print sum(integers)
else:
	print "Error"
	quit()
