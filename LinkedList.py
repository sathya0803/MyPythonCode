import collections
lst = collections.deque([1, 2, 3, 2, 1])
a = collections.deque(lst)
lst.reverse()
if lst == a: print(1)
else: print(0)

def check(a, p):
    if sum(a) == p:
        return a
    if len(a) > 1:
        for subset in (a[:-1], a[1:]):
            result = check(subset, p)
            if result is not None:
                return result