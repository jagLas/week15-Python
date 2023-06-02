class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def addNode(self, x):
        if x == None: return
        current_node = self.root
        if current_node == None:
            self.root = TreeNode(x)
            return
        while True:
            current_val = current_node.val
            if x < current_val:
                if current_node.left == None:
                    current_node.left = TreeNode(x)
                    break
                current_node = current_node.left
            elif x > current_val:
                if current_node.right == None:
                    current_node.right = TreeNode(x)
                    break
                current_node = current_node.right



        
array_nums = [1,2,3,4,5,6,7]


def rangeSumBST(root, low: int, high: int):
    stack = [root]
    total = 0
    while len(stack) > 0:
        node = stack.pop()
        if node == None:
            continue
        val = node.val
        if val < low:
            stack.append(node.right)
        elif val > high:
            stack.append(node.left)
        else:
            total += val
            stack.append(node.left)
            stack.append(node.right)
    return total

bstVals = [10,5,15,3,7, None ,18]
bst = BST()
for value in bstVals:
    bst.addNode(value)

low = 7
high = 15

print(rangeSumBST(bst.root, low, high))