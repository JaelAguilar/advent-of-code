inputText=open("Day 3//input.txt","r")
valueString="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
points=0
count=0
bag=['','','']
for line in inputText:
    bag[count]=line
    count+=1
    if count>2:
        for item in bag[0]:
            if item in bag[1] and item in bag[2]:
                points+=valueString.index(item)+1
                break
        count=0
print(points)