x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

for i in range(0, x):
    for j in range(0, y):
        for k in range(0, z):
            print(f"{i} {j} {k}")

print(x*y*z)