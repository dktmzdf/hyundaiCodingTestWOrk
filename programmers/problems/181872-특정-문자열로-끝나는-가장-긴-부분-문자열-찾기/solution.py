def solution(myString, pat):
    answer = ""
    searchIndex = myString.rfind(pat)
    answer = myString[:searchIndex] + pat
    return answer
