class Tree:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def evenOdd(root):
    if root is None:
        return 0
    return root.data - evenOdd(root.left) - evenOdd(root.right)


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(6)
root.right.left = Tree(5)
print(evenOdd(root))
