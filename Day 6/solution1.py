inputText=open("Day 6//input.txt","r")

for line in inputText:
    for i in range(len(line)):
        for j in range(4):
            if line[j+i] in line[i:i+4].replace(line[j+i],'',1):
                break
            if j==3:
                print(i+j+1)
                exit()