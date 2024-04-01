class Node:
     def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None

def inorderofTraversal(root):
    if root:
        inorderofTraversal(root.left)
        print(root.key)
        inorderofTraversal(root.right)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)

print("ingitorderofTraversal:")
inorderofTraversal(root)
