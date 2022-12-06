inputText=open("Day 6//input.txt","r")

for line in inputText:
    for i in range(len(line)):
        for j in range(14):
            if line[j+i] in line[i:i+14].replace(line[j+i],'',1):
                break
            if j==13:
                print(i+j+1)
                exit()