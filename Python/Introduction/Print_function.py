import sys
N=int(raw_input())
lst=[]
for i in range(1,N+1):
    lst.append(i)
for i in lst:
    sys.stdout.write(str(i))
