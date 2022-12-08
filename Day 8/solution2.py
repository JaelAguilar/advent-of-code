inputText=open("Day 8//input.txt","r")
import numpy as np
grid=np.array([])

#Creating array
arrayLength=0
for line in inputText:
    arrayLength=len(line)-1
    for j in range(len(line)-1):
        grid=np.append(grid,int(line[j]))
grid=grid.reshape(arrayLength,arrayLength)


maxScenic=0
#i -> row
#j -> column
# Used brute force
for row in range(grid.shape[0]):
    for column in range(len(grid[row])):
        scenic=[0,0,0,0] #right,left,up,down
        currentTest=grid[row,column]
        #Check right
        for z in grid[row,:column][::-1]:
            scenic[0]+=1
            if z>=currentTest:break
        #Check left
        for z in grid[row,column+1:]:
            scenic[1]+=1
            if z>=currentTest:break
        #Check up
        for z in grid[:row,column][::-1]:
            scenic[2]+=1
            if z>=currentTest:break
        #Check down
        for z in grid[row+1:,column]:
            scenic[3]+=1
            if z>=currentTest:break
            
        #calculate scenic score
        scenicScore=1
        for i in scenic:
            scenicScore*=i
        maxScenic=max(scenicScore,maxScenic)
            
print(maxScenic)





