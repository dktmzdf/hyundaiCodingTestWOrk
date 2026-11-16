def solution(my_string):
    answer = []
    ss = {}

    vowels_dic = {
        "a": 1,
        "e": 1,
        "i": 1,
        "u": 1,
        "o": 1,
    }

    for c in my_string:
        if vowels_dic.get(c, 0) != 1:
            answer.append(c)

    return "".join(answer)
