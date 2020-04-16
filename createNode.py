class createNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
def sink(first):
    if first is None or (first.left is None and first.right is None): return
    if first.left and first.left.data % 2 == 0:
        first.data, first.left.data = first.left.data, first.data
        sink(first.left)
    elif first.right and first.right.data % 2 == 0:
        first.data, first.right.data = first.right.data, first.data
        sink(first.right)
def sinkNodes(begin):
    if begin is None or (begin.left is None and begin.right is None): return
    sinkNodes(begin.left)
    sinkNodes(begin.right)
    if begin.data % 2 == 1: sink(begin)
def levOrder(x):
    q = [x]
    while len(q):
        y = len(q)
        while y:
            node = q[0]
            print(node.data, end=" ")
            q.pop(0)
            if node.left is not None: q.append(node.left)
            if node.right is not None: q.append(node.right)
            y -= 1
        print()
root = createNode(1)
root.left = createNode(5)
root.right = createNode(8)
root.left.left = createNode(2)
root.left.right = createNode(4)
root.right.left = createNode(9)
root.right.right = createNode(10)
print("Before:")
levOrder(root)
sinkNodes(root)
print("\nAfter:")
levOrder(root)
