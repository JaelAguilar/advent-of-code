inputText=open("Day 9//input.txt","r")
visited=[]
rope=[[0,0] for i in range(10)]

def getClose(Head,Knot):
    if abs(Head[0]-Knot[0])<=1 and abs(Head[1]-Knot[1])<=1:
        return Knot
    for i in [0,1]:
        if Head[i]-Knot[i]>0: #Muy abajo o derecha
            Knot[i]+=1
        elif Head[i]-Knot[i]<0: #Muy arriba o izquierda
            Knot[i]-=1
    return Knot
    

for line in inputText:
    d,step=line[:-1].split(' ')
    for i in range(int(step)):
        H=rope[0]
        if d=="R":H[1]+=1 #right
        elif d=="L":H[1]-=1 #Left
        elif d=="U":H[0]-=1 #UP
        elif d=="D":H[0]+=1 #down
        for knotIndex in range(1,10):
            rope[knotIndex]=getClose(rope[knotIndex-1],rope[knotIndex])    
        visited.append(','.join([str(j) for j in rope[-1]]))
  
print("Total:",len(set(visited)))
