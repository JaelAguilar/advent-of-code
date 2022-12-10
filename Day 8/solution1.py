import numpy as np
import math
inputText=open("Day 8//input.txt","r")
count=0
grid=np.array([int(character) for line in open("Day 8//input.txt").read().split('\n') for character in line])

arrayLength=int(math.sqrt(grid.shape[0]))
grid=grid.reshape(arrayLength,arrayLength)


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