import collections

lst1 = collections.deque([12, 6, 29])
lst2 = collections.deque([23, 5, 8])
lst3 = collections.deque([90, 20, 59])
lst2 = sorted(lst2, reverse=False)
lst3 = sorted(lst3, reverse=True)
s = 41


def check(p):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            for k in range(len(lst3)):
                res = lst1[i] + lst2[j] + lst3[k]
                if res == p:
                    print("Triplets are:", lst1[i], " ", lst2[j], " ", lst3[k])
                    return True
                elif res < p:
                    break
                else:
                    continue

    print('No Triplets found')
    return False


check(s)
