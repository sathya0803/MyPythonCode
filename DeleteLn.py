import collections
lst = collections.deque([1, 2, 3, 4, 5])
print(lst)
while len(lst) != 0:
    lst.pop()
    print(lst)
