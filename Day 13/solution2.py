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

queue=[[[2]],[[6]]]
for line in inputText:
    left_input,right_input=line.split('\n')
    left=ast.literal_eval(left_input)
    right=ast.literal_eval(right_input)
    queue.append(left)
    queue.append(right)

def merge_sort(initialList):
    list_length = len(initialList)

    if list_length == 1:
        return initialList

    mid = list_length // 2

    left = merge_sort(initialList[:mid])
    right = merge_sort(initialList[mid:])
    
    return merge(left, right)


def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if decode(left[i],right[j]):
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output
    
  
queue=merge_sort(queue)
print((queue.index([[2]])+1)*(queue.index([[6]])+1) )