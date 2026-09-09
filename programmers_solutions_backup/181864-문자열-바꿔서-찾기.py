def solution(myString, pat):
    reverseMyString = ["B" if stringChr == "A" else "A" for stringChr in myString]
    return 1 if pat in "".join(reverseMyString) else 0
