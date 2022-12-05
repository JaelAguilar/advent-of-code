inputText=open("Day 2//input.txt","r")
moves="ABC"
points=0

for line in inputText:
    opponentPlay,resultPlay=line[:-1].split(" ")
        
    #Lose
    if resultPlay=="X":
        points+=((moves.index(opponentPlay)+2)%3)+1
    #Draw
    elif resultPlay=="Y":
        points+=moves.index(opponentPlay)+1+3
    #Win
    else:
        points+=(moves.index(opponentPlay)+1)%3+1+6
print(points)