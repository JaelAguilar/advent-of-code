from anytree import Node,RenderTree,find_by_attr,PreOrderIter
import re
inputText=open("Day 7//input.txt","r")
root=Node('/')

for line in inputText:
    line=line.replace('\n','')
    # Command
    if "$ ls" in line:continue
    if "cd" in line:
        parent=line.replace('$ cd ','')
    # Output
    elif "dir" in line:
        folder=line.replace('dir ','')
        Node(folder,parent=find_by_attr(root,parent))
    else:
        file=re.findall('\d+',line)[0]
        Node(file,parent=find_by_attr(root,parent))
        
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
    