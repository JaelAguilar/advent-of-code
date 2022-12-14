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

sand=[]

minimumHeight=max([i[1] for i in rocks])

overflowing=False

while not overflowing:
    currentSand=(500,0)
    
    isSettled=False
    while not isSettled:
        x,y=currentSand
        if y>=minimumHeight:
            overflowing=True
            isSettled=True
        if (x,y+1) not in sand and (x,y+1) not in rocks: #down
            currentSand=(x,y+1)
        
        elif (x-1,y+1) not in sand and (x-1,y+1) not in rocks: #left
            currentSand=(x-1,y+1)
            
        elif (x+1,y+1) not in sand and (x+1,y+1) not in rocks: #right
            currentSand=(x+1,y+1)
        else:
            sand.append(currentSand)
            isSettled=True
        
print(len(sand))
        