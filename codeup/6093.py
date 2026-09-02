n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

d = []  

for i in range(n) :  #0부터 n-1까지...
  d.append(int(a[i]))       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d.reverse()

for i in range(n) :  #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')