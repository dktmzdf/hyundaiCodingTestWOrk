def solution(progresses, speeds):
    answer = []
    jobProgress = 0
    while True:
        for idx in range(0, len(speeds)):
            progresses[idx] += speeds[idx]

        tempJobProgress = jobProgress
        # print(jobProgress)
        for progressIndex in range(tempJobProgress, len(progresses)):
            if progresses[progressIndex] >= 100:
                jobProgress += 1
            else:
                break

        if (jobProgress - tempJobProgress) != 0:
            answer.append(jobProgress - tempJobProgress)

        if len(progresses) == jobProgress:
            break
    return answer
