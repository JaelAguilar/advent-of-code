inputText=open("Day 3//input.txt","r")
valueString="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
points=0
for line in inputText:
    b1=line[slice(0,len(line)//2)]
    b2=line[slice(len(line)//2,len(line))]
    for item in b1:
        if item in b2:
            points+=valueString.index(item)+1
            break
            
print(points)
            