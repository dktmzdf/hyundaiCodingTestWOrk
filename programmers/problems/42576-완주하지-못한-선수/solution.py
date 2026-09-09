from webbrowser import get


def solution(participant, completion):
    answer = ""
    dic_completion = {}
    for i in completion:
        if i in dic_completion:
            dic_completion[i] += 1
        else:
            dic_completion[i] = 1

    for i in participant:
        if dic_completion.get(i, -1) <= 0:
            answer = i
            break
        # elif dic_completion.get(i, -1) > 0:
        #     dic_completion[i] -= 1
        else:
            dic_completion[i] -= 1

    return answer
