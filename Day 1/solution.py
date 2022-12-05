inputText=open("Day 1//input.txt","r")
def solution1():
    maxCalories,currentCalories=0,0
    for line in inputText:
        try:
            currentCalories+=int(line)
        except:
            if line=="\n":
                if currentCalories>maxCalories:
                    maxCalories=currentCalories
                currentCalories=0        
    print(maxCalories)

def solution2():
    maxCalories=[]
    currentCalories=0
    for line in inputText:
        try:
            currentCalories+=int(line)
        except:
            if line=="\n":
                maxCalories.append(currentCalories)
                currentCalories=0  
    maxCalories.sort(reverse=True)     
    print(maxCalories)
    print(sum(maxCalories[0:3]))

