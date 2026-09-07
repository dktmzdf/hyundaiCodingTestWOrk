def solution(arr, k):
    answer = []
    #["B" if stringChr == "A" else "A" for stringChr in myString] 
    if k % 2 == 1:
        answer = [i * k for i in arr]
    if k % 2 == 0:
        answer = [i + k for i in arr]
    return answer
