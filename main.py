class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root == None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def height(root):
    if root == None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1

def balance_factor(root):
    if root == None:
        return 0
    else:
        return height(root.left) - height(root.right)
    
def isAvl(root):
    if root == None:
        return False
    
    balance = balance_factor(root)
    if balance > 1 or balance < -1:
        return False
    
    return isAvl(root.left) and isAvl(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

integersList = [45, 27, 67, 36, 56, 15, 75, 31, 53, 39, 64]

r = Node(integersList[0])
for i in range(1, len(integersList)):
    insert(r, integersList[i])

inorder(r)
print(isAvl(r))