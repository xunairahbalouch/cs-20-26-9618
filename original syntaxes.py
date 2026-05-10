queue = [None for i in range(10)]
headpointer = 0
tailpointer = -1
maxsize = 10
numitems = 0

def enqueue(item):
    global tailpointer, numitems
    if numitems  < maxsize:
        tailpointer +=1
        if tailpointer == maxsize:
            tailpointer = 0
        queue[tailpointer] = item
        numitems +=1
    else: 
        print("queue is full")

def dequeue():
    global headpointer, numitems
    if numitems == 0:
        print("the queue is empty")
    else:
        item = queue[headpointer]
        headpointer = headpointer + 1
        if headpointer == 10:
            headpointer = 0
    numitems = numitems -1
    return item


class Node:
    def __init__(self, data):
        self.data = data
        self.left = -1
        self.right = -1

tree = [Node(-1) for i in range(20)]
rootPointer = -1
freePointer = 0 # Points to the next empty space in the array

def insert(newItem):
    global rootPointer, freePointer
    if rootPointer == -1: # Tree is empty, make this the root
        tree[freePointer].data = newItem
        rootPointer = freePointer
        freePointer += 1
    else:
        curr = rootPointer
        placed = False
        while not placed:
            if newItem < tree[curr].data: # Should it go left?
                if tree[curr].left == -1: # Is the left side empty?
                    tree[curr].left = freePointer
                    tree[freePointer].data = newItem
                    freePointer += 1
                    placed = True
                else:
                    curr = tree[curr].left # Move down to the next node on the left
            else: # Should it go right?
                if tree[curr].right == -1:
                    tree[curr].right = freePointer
                    tree[freePointer].data = newItem
                    freePointer += 1
                    placed = True
                else:
                    curr = tree[curr].right # Move down to the next node on the right
    



def insert(newItem):
    global rootPointer, freePointer # We need to modify these global variables

    # --- STEP 1: Handle the very first insertion ---
    if rootPointer == -1: # If the tree is currently empty
        tree[freePointer].data = newItem # Put the new item in the first available box
        rootPointer = freePointer        # This box is now our root!
        freePointer += 1                 # Move the free pointer to the *next* empty box
        return # We're done with this insertion

    # --- STEP 2: If the tree is NOT empty, we need to find where to put it ---
    else:
        currentPointer = rootPointer # Start at the root of the tree
        placed = False               # Flag to know when we've successfully placed the item

        while not placed: # Keep looping until the item is placed
            # --- Decision Point: Go Left or Go Right? ---
            if newItem < tree[currentPointer].data:
                # The new item is SMALLER, so it belongs in the LEFT subtree

                # --- Check if the LEFT child slot is empty ---
                if tree[currentPointer].left == -1:
                    # YES, it's empty! This is where we put the new node.
                    tree[currentPointer].left = freePointer # Point the current node's left pointer to the free box
                    tree[freePointer].data = newItem        # Put the new item in that free box
                    freePointer += 1                        # Move the free pointer to the *next* empty box
                    placed = True                           # We are done, exit the loop
                else:
                    # NO, the left slot is NOT empty. We need to move down the tree.
                    currentPointer = tree[currentPointer].left # Follow the left pointer to the next node
            else:
                # The new item is GREATER THAN OR EQUAL TO, so it belongs in the RIGHT subtree

                # --- Check if the RIGHT child slot is empty ---
                if tree[currentPointer].right == -1:
                    # YES, it's empty! This is where we put the new node.
                    tree[currentPointer].right = freePointer # Point the current node's right pointer to the free box
                    tree[freePointer].data = newItem         # Put the new item in that free box
                    freePointer += 1                         # Move the free pointer to the *next* empty box
                    placed = True                            # We are done, exit the loop
                else:
                    # NO, the right slot is NOT empty. We need to move down the tree.
                    currentPointer = tree[currentPointer].right # Follow the right pointer to the next node   


# graphs (adjasect method)
# 0 means no connection, 1 means a connection exists
# Create a 5x5 matrix
#Graphs are usually represented as a 2D array. adjMatrix[row][col].

adjMatrix = [[0 for i in range(5)] for j in range(5)]

def addEdge(u, v):
    # For an undirected graph
    adjMatrix[u][v] = 1
    adjMatrix[v][u] = 1

# Example: Connect Node 0 to Node 1
addEdge(0, 1)

#hash tables
hashTable = [None for i in range(10)]

def hashFunction(value):
    return value % 10

def insertHash(value):
    index = hashFunction(value)
    # Linear Probing: find next empty slot
    while hashTable[index] is not None:
        index += 1
        if index >= 10:
            index = 0 # Wrap around to start
    hashTable[index] = value

def findHash(value):
    index = hashFunction(value)
    startIndex = index
    while hashTable[index] != value:
        index += 1
        if index >= 10:
            index = 0
        if index == startIndex: # We searched the whole table
            return -1 # Not found
    return index


#queues
queue = [None for i in range(10)]
headPointer = 0
tailPointer = -1
numItems = 0
maxSize = 10

def enqueue(item):
    global tailPointer, numItems
    if numItems < maxSize:
        tailPointer += 1
        if tailPointer == maxSize: # Circular queue logic (optional but good)
            tailPointer = 0
        queue[tailPointer] = item
        numItems += 1
    else:
        print("Queue Full")

def dequeue():
    global headPointer, numItems
    if numItems == 0:
        print("Queue Empty")
        return None
    else:
    # 2. Grab the data from the current head
        item = queue[headPointer]
# 3. Move the headPointer to the next person in line
        headPointer += 1
        if headPointer == maxSize:
            headPointer = 0
        numItems -= 1
        return item
    

#stack
# global variables
stack = [None for i in range(10)] # Static array of size 10
topPointer = -1 # Points to the current top item
maxSize = 10

def push(item):
    global topPointer
    if topPointer < maxSize - 1:
        topPointer += 1
        stack[topPointer] = item
    else:
        print("Stack Overflow")

def pop():
    global topPointer
    if topPointer == -1:
        print("Stack Underflow")
        return None
    else:
        item = stack[topPointer]
        stack[topPointer] = None # Optional: clear the spot
        topPointer -= 1
        return item
    
    class Node:
    def __init__(self, data, nextnode):
        self.data = data 
        self.nextnode = nextnode

linkedlist = [Node(0, x + 1 ) for x in range(9)] + [Node(0, -1)]
StartPointer = -1
EmptyPointer = 0 

def addnode(item):
    global StartPointer, EmptyPointer
    if EmptyPointer == -1:
        print("list is full")
    else:
        newnode = EmptyPointer
        linkedlist[newnode].data = item 
        EmptyPointer = linkedlist[newnode].nextnode
        linkedlist[newnode].nextnode = StartPointer
        StartPointer = newnode


#traversal (outputting the list)

def print_list():
    current = StartPointer
    if current == -1:
        print("list is empty")
    while current!= -1:
        print(linkedlist[current].data)
        current = linkedlist[current].nextnode




def deleteNode(ValueToDelete):
    global StartPointer, FreePointer, LinkedList
    
    CurrentPointer = StartPointer
    PreviousPointer = -1 # Used to keep track of the node before the one to delete

    # 1. Search for the node
    while CurrentPointer != -1 and LinkedList[CurrentPointer].Data != ValueToDelete:
        PreviousPointer = CurrentPointer
        CurrentPointer = LinkedList[CurrentPointer].NextNode

    # 2. If node was found
    if CurrentPointer != -1:
        # Case A: It's the first node in the list
        if PreviousPointer == -1:
            StartPointer = LinkedList[CurrentPointer].NextNode
        # Case B: It's in the middle or end
        else:
            LinkedList[PreviousPointer].NextNode = LinkedList[CurrentPointer].NextNode

        # 3. Add the node back to the Free List (Recycle it)
        LinkedList[CurrentPointer].Data = None # Clear data
        LinkedList[CurrentPointer].NextNode = FreePointer
        FreePointer = CurrentPointer
        print(f"Value {ValueToDelete} deleted.")
    else:
        print("Value not found in the list.")