N = int(raw_input().strip())
num = [int(i) for i in raw_input().strip().split()]
if 1 <= N <= 10:
	print sum(num)
else:
	print "N is out of range"
	quit()