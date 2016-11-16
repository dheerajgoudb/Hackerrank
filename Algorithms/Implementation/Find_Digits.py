t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    x = [int(i) for i in list(str(n))]
    count = 0
    for j in x:
        if j !=0 and n % j == 0:
            count += 1
    print count
	#print len([j for j in x if j!=0 and n%j==0])
