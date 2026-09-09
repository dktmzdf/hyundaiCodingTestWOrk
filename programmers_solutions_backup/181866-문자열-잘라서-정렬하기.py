def solution(myString):
    parts = myString.split("x")
    answer = [s for s in parts if s != ""]
    return sorted(answer)
