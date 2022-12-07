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
        folder=line.replace('dir ','')
        Node(folder,parent=parent)
    else:
        file=re.findall('\d+',line)[0]
        Node(file,parent=parent)
        
for pre, _, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
        
def obtainSize(subtree):
    sum=0
    for i in subtree.children:
        try:
            sum+=int(i.name)
        except:
            sum+=obtainSize(i)
    return(sum)
    
total=0
for node in PreOrderIter(root):
    size=obtainSize(node)
    if size<=100000:
        total+=size
    
print(total)
    