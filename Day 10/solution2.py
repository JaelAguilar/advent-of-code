inputText=open("Day 10//input.txt","r").read().split('\n')

cycles=0
X=1
CRT=[]
passedCheck=[]

def moveSignal(line):
    if line!="noop":
        dummy,move=line.split(' ')
        move=int(move)
        return move
    
def drawSignal(sprite,X,CRT):
    if sprite[1]%40==0:
        CRT.append('\n')
    CRT.append('#' if X in [i%40 for i in sprite] else '.')
    return CRT
    
for line in inputText:
    sprite=[cycles+i for i in [-1,0,1]]
    if line=="noop":
        #Start cycle noop
        CRT=drawSignal(sprite,X,CRT)
        cycles+=1
        #End cycle
    else:
        # Start first cycle addx
        CRT=drawSignal(sprite,X,CRT)                                 
        cycles+=1
        # End cycle
        #Start second cycle addx
        sprite=[cycles+i for i in [-1,0,1]]
        CRT=drawSignal(sprite,X,CRT)
        cycles+=1
        #End cycle
        X+=moveSignal(line)
    
print(''.join(CRT))