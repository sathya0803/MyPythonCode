import itertools
import collections
l = collections.deque([6, -6, 4, 8, -12, 9, 3, -3])
def check(s):
    if sum(l) == 0:
        print(" no ele need to be rem")
        return
    c = 0
    n = 1
    while c == 0:

        for i in list(itertools.combinations(s, n)):
            if sum(l) - sum(i) == 0:
                print(i)
                c = 1
                break;
        n += 1
check(l)