class DiffOENode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dif(roo):
    if roo is None:
        return 0

    a = [roo]
    odele = 0
    evie = 0
    level = 0

    while len(a):
        s = len(a)
        level += 1
        while s > 0:
            current = a[0]
            a.pop(0)
            if level % 2 == 0:
                evie += current.data
            else:
                odele += current.data

            if current.left:
                a.append(current.left)
            if current.right:
                a.append(current.right)
            s -= 1
    return odele - evie


root = DiffOENode(1)
root.left = DiffOENode(2)
root.right = DiffOENode(3)
root.left.left = DiffOENode(4)
root.right.left = DiffOENode(5)
root.right.right = DiffOENode(6)
print(dif(root))
