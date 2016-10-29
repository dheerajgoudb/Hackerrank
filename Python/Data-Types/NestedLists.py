det = {}
N = int(raw_input())
if 2<=N<=5:
	for i in range(0,N):
		x = raw_input()
		det[x] = float(raw_input())
else:
	print "Value of 'N' is out of range"
	quit()
tmp = zip(det.keys(),[int(i) for i in det.values()])
details = [list(i) for i in tmp]
min2 = sorted(list(set(det.values())))[1]
names2 = []
for a,b in det.items():
	if b == min2:
		names2.append(a)
for i in sorted(names2):
	print i
