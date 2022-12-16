import re
from tqdm import tqdm
inputText=open("Day 15//input.txt").read().split('\n')
minX=minY=0
maxX=maxY=4000000

sensors={}

for line in tqdm(inputText):
    x1,y1,x2,y2=[int(i) for i in re.findall(r'[-]?\d+',line)]
    distance=abs(x1-x2)+abs(y1-y2)
    sensors[(x1,y1)]=distance
    
def checkIfOutside(x,y):
    for sensor in sensors:
        calcDistance=abs(sensor[0]-x)+abs(sensor[1]-y)
        if calcDistance<=sensors[sensor]:
            return False
    return True

def obtainPerimeter(index):
    distance=sensors[index]+1
    result=set()
    X,Y=index[0],index[1]
    for i in range(distance+1):
        for j in [(X+i,Y-distance+i),(X+distance-i,Y+i),(X-i,Y+distance-i),(X-distance+i,Y-i)]:
            result.add(j)
    return result
    

for sensor in tqdm(sensors):
    perimeter=obtainPerimeter(sensor)
    for i_x,i_y in perimeter:
        if i_x<minX or i_y<minY or i_x>maxX or i_y>maxY:
            continue
        if checkIfOutside(i_x,i_y):
            print(i_x,i_y)
            print(i_x*4000000+i_y)
            exit()