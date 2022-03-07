class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            
        def search(self, target):
            if self.data == target:
                print("Found it!")
                return self
            
            if self.left and self.data > target:
                return self.left.search(target)
            
            if self.right and self.data < target:
                return self.right.search(target)
            
            print("value is not it tree")
        
        def traversePreorder(self):
            print(self.data)
            if self.left:
                self.traversePreorder() 
            if self.right:
                self.right.traverPreorder()
            
        def traverseInorder(self):
            if self.left:
                self.left.traverseInroder()
            print(self.data)
            if self.right:
                self.right.traverseInroder()
            
        def traversePostorder(self):
            if self.left:
                self.left.traversePostorder()
            if self.right:
                self.right.traversePostorder()
            print(self.data)
            
class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name
    
    def search(self, target):
        return self.root.search(target)
    
    def traversePreorder(self):
        self.root.traversePreorder()
        
    def traverseInorder(self):
        self.root.traverseInorder()
        
    def traversePostorder(self):
        self.root.traversePostorder()
        
myTree = Tree(Node(50), 'Tree traversals')
myTree.root.left = Node(25)
myTree.root.right = Node(75)
myTree.root.left.left = Node(10)
myTree.root.left.right = Node(35)
myTree.root.left.right.left = Node(30)
myTree.root.left.right.right = Node(42)
myTree.root.left.left.left = Node(5)
myTree.root.left.left.right = Node(13)

print("Traverse Pre-Order")
myTree.traversePreorder()

print("\nTraverse In-Order")
myTree.traverseInorder()

print("\nTraverse Post-Order")
myTree.traversePostorder()


## previous search value in tree build

##node = Node(10)
##node.right = Node(15)
##node.left.left = Node (2)
##node.left.right = Node(6)
##node.right.left = Node(13)
##node.right.right = Node(100)
##myTree = Tree(node, "a tree")
##print(myTree.name)
##print(myTree.root.left.data)
##print(myTree.root.right.right.data)
##found = myTree.search(100)
##print(found.data)
    
