def solution(my_string):
    answer = []

    chrDict = {}
    for ASCIIndex in range(0, 26):
        # print(chr(65 + ASCIIndex))
        chrDict[chr(65 + ASCIIndex)] = 0
    for ASCIIndex in range(0, 26):
        # print(chr(97 + ASCIIndex))
        chrDict[chr(97 + ASCIIndex)] = 0

    for myChr in my_string:
        chrDict[myChr] += 1

    for v in chrDict.values():
        answer.append(v)

    return answer
