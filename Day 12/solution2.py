inputText=open("Day 12//input.txt").read().split('\n')
width,height=len(inputText[0]),len(inputText)
asciiValue='abcdefghijklmnopqrstuvwxyz'

def createNode(letter,x,y,height=height,width=width,ascii=asciiValue):
    neighbors=[]
    if x>0: neighbors.append(str(x-1)+':'+str(y))
    if y>0: neighbors.append(str(x)+':'+str(y-1))
    if x<width-1: neighbors.append(str(x+1)+':'+str(y))
    if y<height-1: neighbors.append(str(x)+':'+str(y+1))
    distance=float('inf')
    try: 
        value=ascii.index(letter)
    except:
        value=ascii.index('a' if letter=='S' else 'z')
    return{'neighbors':neighbors,'distance':distance,'value':value}
    
#Creation of graph
graph={}

for y in range(len(inputText)):
    for x in range(len(inputText[y])):
        nodeName = str(x)+':'+str(y)
        newNode=createNode(inputText[y][x],x,y)
        graph[nodeName]=newNode
        if inputText[y][x]=='E':
            end=nodeName
        
def shortestPath(graph,end):
    path_list=[[end]]
    path_index=0
    previousNodes={end} #avoids revisiting already checked nodes
    if graph[end]['value']==0:
        return path_list[0]
    while path_index<len(path_list):
        currentPath=path_list[path_index]
        lastNode = currentPath[-1]
        #print("\nNode tested",lastNode)
        nextNodes = graph[lastNode]['neighbors']
        #print("Node neighbors",nextNodes)
        if graph[lastNode]['value']==0:
            return currentPath
        for nextNode in nextNodes:
            #print("Next node tested",nextNode)
            if nextNode not in previousNodes and graph[nextNode]['value']>=graph[lastNode]['value']-1:
                #print("node success:",nextNode)
                newPath=currentPath[:]
                
                newPath.append(nextNode)
                #print("New path:",newPath)
                path_list.append(newPath)
                previousNodes.add(nextNode)
        path_index+=1
    

finalPath=shortestPath(graph,end)
print("Path:",finalPath)
print(len(finalPath)-1) #Remove end value
