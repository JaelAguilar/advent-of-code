inputText=open("Day 14//input.txt").read().split('\n')

# Save rocks position
rocks=[]
for line in inputText:
    coordinates=line.split(' -> ')
    for i in range(len(coordinates)-1):
        x1,y1=[int(i) for i in coordinates[i].split(',')]
        x2,y2=[int(i) for i in coordinates[i+1].split(',')]
        if x1==x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                rocks.append((x1,y))
        if y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                rocks.append((x,y1))
rocks=set(rocks)

minimumHeight=max([i[1] for i in rocks])+1

sandPath=[(500,0)]
path_index=0
while True:
    x,y=sandPath[path_index]
    if y>=minimumHeight:break
    for a,b in ((x-1,y+1),(x,y+1),(x+1,y+1)):
        if (a,b) not in rocks and (a,b) not in sandPath:
            sandPath.append((a,b))
    path_index+=1
        
print(len(set(sandPath)))