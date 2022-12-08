inputText=open("Day 8//input.txt","r")
gridTransverse=[]
probablyRight=[]
count=0

i=0
for line in inputText:
    for j in range(len(line)-1):
        try:
            gridTransverse[j].append(line[j])
        except:
            gridTransverse.append([]) 
            gridTransverse[j].append(line[j])       
        if (max(line[:j+1])==line[j] and line[j] not in line[:j]) or (max(line[j:])==line[j] and line[j] not in line[j+1:]) or j==0 or i==0 or j==len(line)-2 or i==len(line)-2:
            count+=1
        else:
            probablyRight.append(str(i)+","+str(j))
    i+=1

for p in probablyRight:
    j,i=[int(i) for i in p.split(',')]
    test=gridTransverse[i][j]    
    if (max(gridTransverse[i][:j+1])==test and test not in gridTransverse[i][:j])  or (max(gridTransverse[i][j:])==test and test not in gridTransverse[i][j+1:]):
        count+=1
print(count)