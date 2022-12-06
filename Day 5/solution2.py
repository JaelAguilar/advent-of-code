import re
inputText=open("Day 5//input.txt","r")
crates=[]

crate_count=0
for line in inputText:
    #Format input for easier manipulation
    line=line.replace("    ","   ")
    line=line.replace("] ","]")
    if "1" in line:
        break
    for i in range(int(len(line)/3)):
        if i+1>len(crates):
            crates.append('')
        supply=line[i*3:(i+1)*3]
        crates[i]+=supply[1]

crates=[i[::-1].replace(" ","") for i in crates] #Reverse all strings adn delete whitespaces

for line in inputText:
    if "move" in line:
        moves=[int(i) for i in re.findall(r'\d+',line)]
        # Long line, but basically takes the last X characters of the first crate, and appends them to the second crate. For this solution it is not necessary to reverse the items
        crates[moves[2]-1] += crates[moves[1]-1][moves[0]*(-1):]
        #Here we just remove the last X characters of the first crate 
        crates[moves[1]-1] = crates[moves[1]-1][:moves[0]*(-1)]

# Print the last characters of every item in the list
print(''.join([i[-1] for i in crates]))
