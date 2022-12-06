inputText=open("Day 1//input.txt","r")

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