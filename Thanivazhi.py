def check(a):
    while a % 2 == 0:
        a = a // 2
    while a % 3 == 0:
        a = a // 3
    while a % 5 == 0:
        a = a // 5
    if a == 1 and a > 0:
        return True
    return False


def sort():
    a = [13, 9, 11, 3, 2]
    v = []
    for i in range(len(a)):
        if check(a[i]):
            v.append(a[i])
            a[i] = 0
    v.sort()
    j = 0
    for i in range(len(a)):
        if a[i] == 0:
            print(v[j])
            j += 1
        else:
            print(a[i])


sort()
