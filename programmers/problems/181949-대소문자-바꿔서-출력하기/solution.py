str = input()

convertStr = []

for i in range(0, len(str)) :
    if ord('a') > ord(str[i]) :
        convertStr.append(chr(ord(str[i]) + 32))
    else :
        convertStr.append(chr(ord(str[i]) - 32))

print(''.join(convertStr))
#c = ord(input()) # A->65
#print(chr(c+1))  # 66->B
