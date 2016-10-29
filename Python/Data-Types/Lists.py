N=int(raw_input())
lst=list()
for i in range(N):
    x=raw_input().strip()
    x=x.split()
    com=x[0]
    x.remove(x[0])
    if com=='print': 
        print lst
    elif com=='append': 
        lst.append(int(x[0]))
    elif com=='insert':
        i=int(x[0])
        n=int(x[1])
        lst.insert(i,n)
    elif com=='remove':
        lst.remove(int(x[0]))
    elif com=='sort':
        lst.sort()
    elif com=='pop':
        lst.pop()
    elif com=='reverse':
        lst.reverse()
