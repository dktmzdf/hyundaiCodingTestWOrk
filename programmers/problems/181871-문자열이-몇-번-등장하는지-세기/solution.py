def solution(myString, pat):

    searchIndex = 0
    count = 0
    while searchIndex != len(myString):
        sliceStr = myString[searchIndex:]

        count += 1 if sliceStr.startswith(pat) else 0
        if searchIndex == len(myString):
            break
        searchIndex += 1

    return count
