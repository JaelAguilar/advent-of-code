inputText=open("Day 2//input.txt","r")
# A,X = rock
# B,Y = paper
# C,Z = scissors
moves={"A":0,"B":1,"C":2,"X":0,"Y":1,"Z":2}
points=0


for line in inputText:
        opponentPlay,myPlay=line[:-1].split(" ")
        print(moves[myPlay],moves[opponentPlay],sep=", ")
        points+=moves[myPlay]+1
        if moves[myPlay]==moves[opponentPlay]:
            points+=3
        elif moves[myPlay]==(moves[opponentPlay]+4)%3:
            points+=6

print(points)

# WRONG
# 19603 high
# 10105 low
# 7273 low