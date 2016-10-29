n=int(raw_input())
dic=dict()
lst=list()
for i in range(0,n):
    det=raw_input()
    det=det.split()
    name=det[0]
    lst=[float(x) for x in det[1:]]
    dic[name]=lst
x=raw_input()
avg=0
if x in dic.keys():
    marks=dic[x]
avg=sum(marks)/len(marks)
print "%.2f" %avg
