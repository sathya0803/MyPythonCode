s = "sampathrajakumarraja"
l = list(s)
print(s)
for i in range(len(l)-1):
    l = list(s)
    l.insert(i+1, " ")
    print("".join(l))
print(" ".join(list(s)))
