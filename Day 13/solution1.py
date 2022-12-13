import ast
inputText=open("Day 13//input.txt").read().split('\n\n')

def decode(left,right):
    #Caso donde ambos son integers
    if type(left) is int and type(right) is int:
        if right<left:
            return False
        if right>left:
            return True
        else:return 
        
    #Caso donde ambos son listas
    if type(left) is list and type(right) is list:
        left=[i for i in left]
        right=[i for i in right]

        try:
            for i in range(len(left)):
                testing=decode(left[i],right[i])
                #print("Test",testing)
                if testing==True:
                    return True
                if testing==False:
                    return False
            return True
        except:
            return False
    
    # Caso donde uno de los dos es integer
    elif type(right) is int:
        right=[right]
        return decode(left,right)
    elif type(left) is int:
        left=[left]
        return decode(left,right)

index=0
total=0
for line in inputText:
    index+=1
    left_input,right_input=line.split('\n')
    left=ast.literal_eval(left_input)
    right=ast.literal_eval(right_input)
    test=decode(left,right)
    if test:
        total+=index

    
print(total)