S = raw_input()
if 0 < len(S) <= 1000:
	x = list(S)
else:
	print 'Input String length not in range'
	quit()
T = []
for i in x:
	if i == i.lower():
		T.append(i.upper())
	elif i == i.upper():
		T.append(i.lower())
	else:
		T.append(i)
print "".join(T)
