# Write your class here.
class Node:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, current, node):
        if self.head == None:
            self.head = current

        while True:
            if node.val < current.val:
                if current.left == None:
                    current.left = node
                    return 'node inserted'
                else:
                    current = current.left
            elif node.val > current.val:
                if current.right == None:
                    current.right = node
                    return 'node inserted'
                else:
                    current = current.right
            else:
                return 'insertion failed'
            
        


tree = Tree()

root = Node(4)
tree.insert(root, Node(1))
tree.insert(root, Node(2))
tree.insert(root, Node(3))

print("** PRE ORDER: **")
tree.preorder_traversal(root) # 4, 1, 2, 3

print("** IN ORDER: **")
tree.inorder_traversal(root) # 1, 2, 3, 4

print("** POST ORDER: **")
tree.postorder_traversal(root) # 3, 2, 1, 4