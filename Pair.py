a = [4, 5, 7, 11, 9, 13, 8, 12]
N = 20
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == N:  print(a[i], a[j])

class createNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def isLeaf(start):
    return start.left is None and start.right is None


def sink(first):
    if first is None or isLeaf(first):
        return
    if first.left and not first.left.data and 1:
        first.data, first.left.data = first.left.data, first.data
        sink(first.left)
    elif first.right and not first.right.data and 1:
        first.data, first.right.data = first.right.data, first.data
        sink(first.right)


def sinkNodes(begin):
    if begin is None or isLeaf(begin):
        return
    sinkNodes(begin.left)
    sinkNodes(begin.right)
    if begin.data and 1:
        sink(begin)


def levOrder(x):
    q = [x]
    while len(q):
        y = len(q)
        while y:
            node = q[0]
            print(node.data, end=" ")
            q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            y -= 1
        print()


root = createNode(1)
root.left = createNode(2)
root.right = createNode(3)
print("Before:", end=" ")
levOrder(root)
sinkNodes(root)
print("\nAfter:", end=" ")
levOrder(root)
