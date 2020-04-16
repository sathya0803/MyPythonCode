import collections
a = collections.deque([1, 2, 3, 4, 5, 6, 7, 8])
if len(a) % 2 == 0: print(a[len(a)//2-1], a[len(a)//2])
else: print(a[len(a)//2])

