class BinaryTreeNode:
    """Task 2.1: Binary Tree Node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Task 2.1 & 2.2: Binary Search Tree implementation"""
    
    def __init__(self):
        self.root = None
        self.count = 0
    
    def IsEmpty(self):
        """Task 2.1: Check if tree is empty"""
        return self.root is None
    
    def Insert(self, data):
        """Task 2.2: Insert data into BST"""
        new_node = BinaryTreeNode(data)
        
        if self.root is None:
            self.root = new_node
            self.count += 1
            print(f"Inserted {data} as root")
            return True
        
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    self.count += 1
                    print(f"Inserted {data} to left of {current.data}")
                    return True
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    self.count += 1
                    print(f"Inserted {data} to right of {current.data}")
                    return True
                current = current.right
            else:
                print(f"Duplicate value {data}")
                return False
    
    def Search(self, data):
        """Task 2.2: Search for data in BST"""
        current = self.root
        
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        
        return False
    
    def FindMin(self):
        """Task 2.3: Find minimum value"""
        if self.root is None:
            return None
        
        current = self.root
        while current.left is not None:
            current = current.left
        
        return current.data
    
    def FindMax(self):
        """Task 2.3: Find maximum value"""
        if self.root is None:
            return None
        
        current = self.root
        while current.right is not None:
            current = current.right
        
        return current.data
    
    def InOrderTraversal(self, node=None, result=None):
        """Task 2.2: In-order traversal (Left, Root, Right)"""
        if result is None:
            result = []
        
        if node is None:
            node = self.root
        
        if node.left:
            self.InOrderTraversal(node.left, result)
        
        result.append(node.data)
        
        if node.right:
            self.InOrderTraversal(node.right, result)
        
        return result
    
    def PreOrderTraversal(self, node=None, result=None):
        """Task 2.2: Pre-order traversal (Root, Left, Right)"""
        if result is None:
            result = []
        
        if node is None:
            node = self.root
        
        result.append(node.data)
        
        if node.left:
            self.PreOrderTraversal(node.left, result)
        
        if node.right:
            self.PreOrderTraversal(node.right, result)
        
        return result
    
    def PostOrderTraversal(self, node=None, result=None):
        """Task 2.2: Post-order traversal (Left, Right, Root)"""
        if result is None:
            result = []
        
        if node is None:
            node = self.root
        
        if node.left:
            self.PostOrderTraversal(node.left, result)
        
        if node.right:
            self.PostOrderTraversal(node.right, result)
        
        result.append(node.data)
        
        return result
    
    def CountNodes(self):
        """Task 2.3: Count total nodes"""
        return self.count
    
    def CountLeaves(self, node=None):
        """Task 2.3: Count leaf nodes"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        return self.CountLeaves(node.left) + self.CountLeaves(node.right)
    
    def CountInternalNodes(self, node=None):
        """Task 2.3: Count internal nodes (non-leaf)"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 0
        
        return 1 + self.CountInternalNodes(node.left) + self.CountInternalNodes(node.right)
    
    def FindHeight(self, node=None):
        """Task 2.3: Find height of tree"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        left_height = self.FindHeight(node.left)
        right_height = self.FindHeight(node.right)
        
        return 1 + max(left_height, right_height)
    
    def Delete(self, data):
        """Task 2.4: Delete a node from BST"""
        parent = None
        current = self.root
        
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        if current is None:
            print(f"Value {data} not found")
            return False
        
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        
        elif current.left is None:
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
        
        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        
        else:
            successor_parent = current
            successor = current.right
            
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            current.data = successor.data
            
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        
        self.count -= 1
        print(f"Deleted {data}")
        return True


def TreeSort(data_list):
    """Task 2.4: Sort using BST"""
    bst = BinarySearchTree()
    
    for item in data_list:
        bst.Insert(item)
    
    return bst.InOrderTraversal()


if __name__ == "__main__":
    bst = BinarySearchTree()
    
    print("=" * 80)
    print("Task 2.1 & 2.2: Binary Search Tree")
    print("=" * 80)
    
    values = [50, 30, 70, 20, 40, 60, 80, 15, 25, 35, 45]
    for val in values:
        bst.Insert(val)
    
    print("\n" + "=" * 80)
    print("Task 2.2: Tree Traversals")
    print("=" * 80)
    print(f"In-order: {bst.InOrderTraversal()}")
    print(f"Pre-order: {bst.PreOrderTraversal()}")
    print(f"Post-order: {bst.PostOrderTraversal()}")
    
    print("\n" + "=" * 80)
    print("Task 2.3: Tree Statistics")
    print("=" * 80)
    print(f"Min value: {bst.FindMin()}")
    print(f"Max value: {bst.FindMax()}")
    print(f"Total nodes: {bst.CountNodes()}")
    print(f"Leaf nodes: {bst.CountLeaves()}")
    print(f"Internal nodes: {bst.CountInternalNodes()}")
    print(f"Height: {bst.FindHeight()}")
    
    print("\n" + "=" * 80)
    print("Task 2.4: Search and Sort")
    print("=" * 80)
    print(f"Search 40: {bst.Search(40)}")
    print(f"Search 100: {bst.Search(100)}")
    
    print(f"\nSorted list: {TreeSort([64, 25, 12, 22, 11, 90])}")
