x, y, z, h = input().split()
x = int(x)
y = int(y)
z = int(z)
h = int(h)

s=x

for i in range(0, h-1) :
    s = s*y+z


print(s)