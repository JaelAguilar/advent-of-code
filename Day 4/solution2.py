inputText=open("Day 4//input.txt","r")

count=0
for line in inputText:
    asig1,asig2=line[:-1].split(",")
    asig1=[int(i) for i in asig1.split("-")]
    asig2=[int(i) for i in asig2.split("-")]
    count+=1
    if(asig1[0]<asig2[0] and asig1[1]<asig2[0]):
        count-=1
    elif(asig1[0]>asig2[1] and asig1[0]>asig2[1]):
        count-=1
        
print(count)