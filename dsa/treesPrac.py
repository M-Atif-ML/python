from collections import deque
class TreeNode:
    def __init__(self,val,left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F




def pre_order_traversal(node):
    if not node:
        return

    print(node)

    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
# pre_order_traversal(A)
# print("----")
def in_order_traversal(node):
    if not node:
        return
    in_order_traversal(node.left)
    print(node)
    in_order_traversal(node.right)
# in_order_traversal(A)

def bfs(node):
    q = deque()

    l = []

    q.appendleft(node)

    while q:
        node = q.pop()
        l.append(node.val)

        if node.right == None and node.left:
            node.right = TreeNode(None)
        if node.left == None and node.right:
            node.left = TreeNode(None)

        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)
    return l

print(bfs(A)





