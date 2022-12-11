import operator
ops={'+':operator.add,'-':operator.sub,'*':operator.mul}
inputText=open("Day 11//input.txt","r").read().split('\n')
monkeys=[[],[],[],[],[],[],[],[]]
monkeyInspection=[]


for round in range(20):
    for line in inputText:
        if 'Monkey' in line:
            currentMonkey=int(line[-2])
        elif 'Starting' in line:
            items=monkeys[currentMonkey]
            if round==0:
                items+=[int(i) for i in line[18:].split(', ')]
            try:
                monkeyInspection[currentMonkey]+=len(items)
            except:
                monkeyInspection.append(len(items))
            monkeys[currentMonkey]=[]
            
        elif 'Operation' in line:
            sign,value=line[23:].split(' ')
            for i in range(len(items)):
                items[i]=int((ops[sign](items[i],items[i] if value=='old' else int(value)))/3)
                
        elif 'Test' in line:
            test=int(line[21:])
            
        elif 'true' in line:
            test_true=int(line[-1])
        elif 'false' in line:
            test_false=int(line[-1])
            for z in items: 
                monkeys[test_true if z%test==0 else test_false].append(z)
            
monkeyInspection.sort()
print("Result:",monkeyInspection[-1]*monkeyInspection[-2])

#90882