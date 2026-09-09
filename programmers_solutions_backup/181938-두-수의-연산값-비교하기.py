def solution(a, b):
    answer = 0

    temp1 = 2 * a * b;
    temp2 = int(str(a)+str(b))

    if temp1 > temp2:
        answer = temp1;
    else:
        answer = temp2;


    return answer
