import re
inputText=open("Day 15//input.txt").read().split('\n')
yCheck=2000000
maxX=0
minX=0
impossibles=set()
ogBeacons=set()

for line in inputText:
    x1,y1,x2,y2=[int(i) for i in re.findall(r'[-]?\d+',line)]
    maxX=max(x1,x2,maxX)
    minX=min(x1,x2,minX)
    distance=abs(x1-x2)+abs(y1-y2)
    
    if y2==yCheck:
        ogBeacons.add(x2)
    if abs(y1-yCheck)>distance:#Don't bother checking
        continue
    elif abs(y1-yCheck)==distance:
        newX=distance-abs(yCheck-y1)+x1
        impossibles.add((newX,newX))
    else:
        test=distance-abs(yCheck-y1)
        limit1,limit2=test+x1,test*-1+x1
        first=min(limit1,limit2)
        last=max(limit1,limit2)
        impossibles.add((first,last))
        
   
finalSet=set()
for i in impossibles:
    for j in range(i[0],i[1]+1):
        finalSet.add(j)

finalSet=finalSet.difference(ogBeacons)
print(len(finalSet))
