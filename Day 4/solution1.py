inputText=open("Day 4//input.txt","r")

count=0
for line in inputText:
    asig1,asig2=line[:-1].split(",")
    asig1=[i for i in asig1.split("-")]
    asig2=[i for i in asig2.split("-")]
    if (int(asig1[0])<=int(asig2[0]) and int(asig1[-1])>=int(asig2[-1]))or (int(asig1[0])>=int(asig2[0]) and int(asig1[-1])<=int(asig2[-1])):
        count+=1
        
print(count)