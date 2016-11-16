n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
x,y,z = 0,0,0
l = float(len(arr))
for i in arr:
    if i > 0:
        x+=1
    elif i < 0:
        y+=1
    else:
        z+=1
output = [i/l for i in [x,y,z]]
for i in output:
    print i
