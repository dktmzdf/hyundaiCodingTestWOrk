def solution(myString):
    answer = list(myString.lower())
    for idx in range(len(answer)):
        if answer[idx] == "a":
            answer[idx] = "A"
    return "".join(answer)
