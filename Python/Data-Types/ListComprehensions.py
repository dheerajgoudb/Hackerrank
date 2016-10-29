dimensions = []
for i in range(3):
	dimensions.append(int(raw_input()))
N = int(raw_input())
LIO = [[x,y,z] for x in range(dimensions[0]+1) for y in range(dimensions[1]+1) for z in range(dimensions[2]+1) if x+y+z != N]
print LIO