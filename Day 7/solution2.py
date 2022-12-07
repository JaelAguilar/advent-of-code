from anytree import Node,RenderTree,findall_by_attr,PreOrderIter
import re
inputText=open("Day 7//input.txt","r")
root=Node('/')
parent=root

for line in inputText:
    line=line.replace('\n','')
    # Command
    if ("$ ls" in line) or ("$ cd /" in line):continue
    elif "$ cd .." in line:
        parent=parent.parent
    elif "$ cd" in line:
        parent=findall_by_attr(parent,line.replace('$ cd ',''),maxlevel=2)[-1]
    # Output
    elif "dir " in line:
        Node(line.replace('dir ',''),parent=parent)
    else:
        Node(re.findall('\d+',line)[0],parent=parent)
        
        
def obtainSize(subtree):
    sum=0
    for i in subtree.children:
        try:
            sum+=int(i.name)
        except:
            sum+=obtainSize(i)
    return(sum)

neededSpace=(70000000-30000000-obtainSize(root))*-1
    
results=[]
for node in PreOrderIter(root):
    size=obtainSize(node)
    if size>=neededSpace:
        results.append(size)
    
print(sorted(results)[0])
    