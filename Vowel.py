a = "Regina Phalange"
l = list(a.replace(" ", ""))
v = "aAeEiIoOuU"
c = 0
for i in l:
   if v.__contains__(i): c += 1
print(c)