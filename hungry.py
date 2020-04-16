a: str = "How you Doing"
a = a.replace(" ", "")
a = a.lower()
b = []
c = []
for j in range(len(a)):
    c.append(a.count(a[j]))
    b.append(a[j])
    a.replace(a[j], '')
print("max:", b[c.index(max(c))])
print("min:", b[c.index(min(c))])
