def solution(picture, k):
    answer = []
    for x in picture:
        for repeat in range(k):
            tempStr = ""
            for pixel in x:
                tempStr += pixel * k
            answer.append(tempStr)
    return answer
