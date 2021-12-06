l = list()
x = input()
while x:
    l.append(int(x))
    x = input()


c = 0
for ind, deepth in enumerate(l):
    if ind == 0:
        continue
    if deepth > l[ind - 1]:
        c += 1

print(c)
