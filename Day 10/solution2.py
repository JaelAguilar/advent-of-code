inputText=open("Day 10//input.txt","r").read().split('\n')

#lines=[x for x in open("Day 9//input.txt").read().split('\n')]
cycles=0
X=1
importantCycles=[40,80,120,160,200,240]

CRT=[[],[],[],[],[],[]]
passedCheck=[]


    
def moveSignal(line):
    if line!="noop":
        dummy,move=line.split(' ')
        move=int(move)
        return move
    
def drawSignal(sprite,X,CRT):
    for i in range(len(importantCycles)):
        if sprite[1]<importantCycles[i]:
            verticalIndex=i
    if sprite[1] in passedCheck:
        return CRT
    
    print("v:",verticalIndex)
    print('max:',max(0,sprite[1]//40))
    CRT[max(0,sprite[1]//40)].append('#' if X in [i%40 for i in sprite] else '.')
    passedCheck.append(sprite[0])
    return CRT
    

for line in inputText:
    sprite=[cycles+i for i in [-1,0,1]]
    print(sprite)
    if line=="noop":
        #Start cycle noop
        CRT=drawSignal(sprite,X,CRT)
        cycles+=1
        
        #End cycle
    else:
        print("Cycle in:",cycles,"X:",X)
        # Start first cycle addx
        CRT=drawSignal(sprite,X,CRT)
        cycles+=1
        # End cycle
        #Start second cycle addx
        CRT=drawSignal(sprite,X,CRT)
        cycles+=1
        #End cycle
        X+=moveSignal(line)

    print("Cycle out:",cycles,"X:",X)
    
print('\n'.join([''.join(i) for i in CRT]))