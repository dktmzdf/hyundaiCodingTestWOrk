def solution(numbers):
    # 음....  일단 자리수가 적은 애들부터 가장 큰값을 미루어야 됨 9, 9, 9, 1000 이라고 하면 9991000이 가장 크거든
    # 먼저 따로 배열을 복사후 계산하면서 이미 계산된건 -1로 바꾸면 될듯
    # 잘못 생각함 아무래도 가장 큰 자리수를 가장 큰놈이 정렬해야할듯

    # 설마 파이썬에서 전부 문자열로 바꾸고 정렬하면 알아서 되던가?
    # 아 진짜네;; 이거 문자열로 바꾸고 정렬하면 사전정렬이 되니 알아서 큰게 되는구나;;
    answer = ""
    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            temp_1 = str(numbers[j]) + str(numbers[j - 1])
            temp_2 = str(numbers[j - 1]) + str(numbers[j])
            if temp_1 > temp_2:
                numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            else:
                break
    # print(numbers)
    for n in numbers:
        answer += str(n)
    return answer
