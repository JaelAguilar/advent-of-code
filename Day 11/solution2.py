import operator
ops={'+':operator.add,'-':operator.sub,'*':operator.mul}
inputText=open("Day 11//input.txt","r").read().split('\n')
monkeyInspection=[0,0,0,0,0,0,0,0]

def getInput(input):
    data={}
    for line in input:
        if 'Monkey' in line:
            currentMonkey=int(line[-2])
            data[currentMonkey]={}
        elif 'Starting' in line:
            data[currentMonkey]['items']=[int(i) for i in line[18:].split(', ')]
        elif 'Operation' in line:
            data[currentMonkey]['operation']=line[23:].split(' ')
        elif 'Test' in line:
            data[currentMonkey]['test']=int(line[21:])
        elif 'true' in line:
            data[currentMonkey]['true']=int(line[-1])
        elif 'false' in line:
            data[currentMonkey]['false']=int(line[-1])
    return data
    
def getLCM(data):
    result=1
    for i in range(len(data)):
        result*=data[i]['test']
    return result

monkeys=getInput(inputText)
LCM = getLCM(monkeys)


for round in range(10000):
    for monkey in monkeys:
        items=monkeys[monkey]['items']
        sign,value=monkeys[monkey]['operation']
        test=monkeys[monkey]['test']
        test_true=monkeys[monkey]['true']
        test_false=monkeys[monkey]['false']   

        monkeyInspection[monkey]+=len(items)

        monkeys[monkey]['items']=[]
        
        for i in range(len(items)):
            items[i]=(ops[sign](items[i],items[i] if value=='old' else int(value)))%LCM
            
            monkeys[test_true if items[i]%test==0 else test_false]['items'].append(items[i])
            


monkeyInspection.sort()
print("Result:",monkeyInspection[-1]*monkeyInspection[-2])

