class linkedlistnode:
    def __init__(self,value,nextnode=None):
        self.value = value
        self.nextnode = nextnode 

node1 = linkedlistnode("3")
node2 = linkedlistnode("4")
node3 = linkedlistnode("7")

node1.nextnode = node2   #connecting nodes
node2.nextnode = node3 

currentnode = node1 

while True:
    print(currentnode.value)
    if currentnode.nextnode is None:
        print(None)
        break 
    currentnode = currentnode.nextnode
    

        