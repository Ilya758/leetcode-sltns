x = [0,1,3]

xx = len(x)

for n in range(len(x)):
    xx ^= n ^ x[n]

print(xx)