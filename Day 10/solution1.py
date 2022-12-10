inputText=open("Day 10//input.txt","r").read().split('\n')
cycles=0
X=1
importantCycles=[20,60,100,140,180,220]
sumStrengths=0

def checkStrength(cycle,value):
    if cycle in importantCycles:
        importantCycles.remove(cycle)
        return cycle*value
    return 0
    
def moveSignal(line):
    if line!="noop":
        dummy,move=line.split(' ')
        move=int(move)
        return move

for line in inputText:
    if line=="noop":
        sumStrengths+=checkStrength(cycles,X)
        cycles+=1
    else:
        cycles+=1
        sumStrengths+=checkStrength(cycles,X)
        cycles+=1
        sumStrengths+=checkStrength(cycles,X)
        X+=moveSignal(line)
    
print(sumStrengths) 