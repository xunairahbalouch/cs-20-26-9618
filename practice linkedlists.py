class Node:
    def __init__(self, data, nextnode):
        self.data = data
        self.nextnode = nextnode
linkedlist = [Node(0, -1) for x in range(9)] + [Node(0, -1)]
StartPointer = -1
EmptyPointer = 0 

def addnode(item):
    global StartPointer, EmptyPointer
    if EmptyPointer == -1:
        print("list is empty")
    else:
        newnode = EmptyPointer
        linkedlist[newnode].data = item
        EmptyPointer = linkedlist[newnode].nextnode
        linkedlist[newnode].nextnode= StartPointer
        StartPointer = newnode
    
#traversal (output the list)
def print_list():
    current = StartPointer
    if current == -1:
        print("list is empty")
    while current!= -1:
        print(linkedlist[current].data)
        current = linkedlist[current].nextnode

#Searching 
def find_node(itemtofind):
    current = StartPointer
    while current!= -1:
        if linkedlist[current].data == itemtofind:
            return current
        current = linkedlist[current].nextnode
    return -1

#deletion
def delete_node(itemtofind):
    global Startpointer, EmptyPointer
    current = StartPointer
    previous = -1 

    while current!= -1 and linkedlist[current].data != itemtofind:
        previous = current 
        current = linkedlist[current].nextnode

    if current == -1:
        print("item not found")
    else:
        #step1, remove from the main list   
            if previous == -1:
                StartPointer = linkedlist[current].nextnode
            else:
                linkedlist[previous].nextnode = linkedlist[current].nextnode

        
#bubblesort

def bubblesort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            swapped = False
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            if not swapped:
                break

mylist = [4,5,3, 6, 7]
bubblesort(mylist)
print(f"scorelist: {bubblesort}")

#insertion sort:
def insertionsort(arr):
    for x in range (1, arr(len)):
        current = arr[x]
        position = x
        while current > 0 and arr[position-1] > current:
            arr[position] = arr[position-1]
            arr[position] = current 

         #insertionsort
def insertionsort(arr):
    for x in range(1, arr(len)):
        current = arr[x]
        position = x

    while current > 0 and arr[position -1] > current:
        arr[position] = arr[position -1]

    arr[position] = current

#bubble sort
def bubbleSort(arr):
    n = len(arr)
    
    # Outer loop goes through the whole list
    for i in range(n - 1):
        swapped = False
        
        # Inner loop compares adjacent elements
        # (n-i-1) because the last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap them using Python's shortcut
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

# Example usage:
myList = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(myList)
print(f"Sorted list: {myList}")
       

#deletion in linkedlist:
#Check if list is empty: If StartPointer is -1, there is nothing to delete.
def deletenode(ValueToDelete):
    global StartPointer, FreePointer, linkedlist
    Current = StartPointer
    Previous = -1
    while Current!= -1 and linkedlist[Current].data!= ValueToDelete:
        Current = Previous
        Current = linkedlist[Current].nextnode

        if Current!= -1:
            if Previous!= -1:
                StartPointer = linkedlist[Current].nextnode






        






