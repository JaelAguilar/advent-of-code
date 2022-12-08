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
for row in range(grid.shape[0]):
    for column in range(len(grid[row])):
        currentTest=grid[row,column]
        sc_index=0
        scenicScore=1
        
        for arrayTest in [grid[row,:column][::-1],grid[row,column+1:],grid[:row,column][::-1],grid[row+1:,column]]: #Testing left, right, up, down
            temp_s=0
            for z in arrayTest:
                temp_s+=1
                if z>=currentTest:break
            scenicScore*=temp_s
        maxScenic=max(scenicScore,maxScenic)
        
            
print(maxScenic)





