#첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
#두 번째 줄에 놓을 수 있는 막대의 개수(n)
#세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
#1 <= w, h <= 100
#1 <= n <= 10
#d = 0 or 1
#1 <= x <= 100-h
#1 <= y <= 100-w

h, w = map(int, input().split())
w=int(w)
h=int(h)
array=[[0 for j in range(w)] for i in range(h)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    l=int(l)
    d=int(d)
    x=int(x)
    y=int(y)
    if d == 0:
        for j in range(l):
            temp=(int)((x-1)*h + (y-1+j))#좌표계산
            #print(temp)
            array[x-1][y-1+j]=1
    else:
        for j in range(l):
            temp=(int)((x-1+j)*h + (y-1))
            #print(temp)
            array[x-1+j][y-1]=1


for j in range(h) :
    for i in range(w) :
        print(array[j][i], end=' ')
    print()