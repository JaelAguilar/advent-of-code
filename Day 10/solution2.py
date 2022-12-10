inputText=[line.split(' ') for line in open("Day 10//input.txt","r").read().split('\n')]

cycles=0
X=1
CRT=[]
passedCheck=[]
    
def drawSignal(sprite,X,CRT):
    if sprite%40==0:
        CRT.append('\n')
    CRT.append('█' if X-1<= sprite%40 <=X+1 else ' ')
    return CRT
    
for line in inputText:
    # Start first cycle
    CRT=drawSignal(cycles,X,CRT)                                 
    cycles+=1
    # End cycle
    if line[0]=='addx':
        #Start second cycle addx
        CRT=drawSignal(cycles,X,CRT)
        cycles+=1
        #End cycle
        X+=int(line[1])
    
    
print(''.join(CRT))