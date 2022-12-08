import numpy as np
inputText=open("Day 8//input.txt","r")
count=0
grid=np.array([])

#Creating array
arrayLength=0
for line in inputText:
    arrayLength=len(line)-1
    for j in range(len(line)-1):
        grid=np.append(grid,int(line[j]))
grid=grid.reshape(arrayLength,arrayLength)
print(grid.shape)

# Analyze trees
for row in range(arrayLength):
    for column in range(arrayLength):
        if row==0 or row==arrayLength-1 or column==0 or column==arrayLength-1:
            count+=1
            continue
        for testArray in [grid[row,:column+1],grid[row,column:],grid[:row+1,column],grid[row:,column]]:
            if max(testArray)==grid[row,column] and np.count_nonzero(testArray==grid[row,column])==1:
                count+=1
                break
print(count)