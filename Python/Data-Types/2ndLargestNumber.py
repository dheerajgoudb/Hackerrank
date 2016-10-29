N = int(raw_input())
num = [int(i) for i in raw_input().split()]
if N != len(num):
	print 'Not matching'
print sorted(list(set(num)))[-2]