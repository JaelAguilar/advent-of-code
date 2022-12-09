inputText=open("Day 9//input.txt","r")
visited=[]
H=[100,100]
T=[100,100]

def getClose(Head,Tail):
    
    if abs(Head[0]-Tail[0])<=1 and abs(Head[1]-Tail[1])<=1:
        return Tail
    for i in [0,1]:
        if Head[i]-Tail[i]>0: #Muy abajo o derecha
            Tail[i]+=1
        elif Head[i]-Tail[i]<0: #Muy arriba o izquierda
            Tail[i]-=1
    return Tail
    

for line in inputText:
    d,step=line[:-1].split(' ')
    for i in range(int(step)):
        if d=="R":H[1]+=1 #right
        elif d=="L":H[1]-=1 #Left
        elif d=="U":H[0]-=1 #UP
        elif d=="D":H[0]+=1 #down
        T=getClose(H,T)
        visited.append(','.join([str(j) for j in T])) #Originally I put this at the beginning of the loop, and I always got the answer wrong even though I was sure the logic was correct. I almost cried when I found the error in my code
        
print("Total:",len(set(visited)))

