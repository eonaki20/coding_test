from collections import deque
import math

def solution(progresses, speeds):

    days = deque([math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))])

    '''최초 배부일(기초값)'''
    distribution_day = [days[0]]
    distribution_num = 1
    days.popleft()
    distribution = []

    while days:
        if days[0] > distribution_day[0]:
            distribution.append(distribution_num)
            distribution_day = [days[0]]
            distribution_num = 1
            days.popleft()
        else:
            distribution_num += 1
            days.popleft()

    distribution.append(distribution_num)
    return distribution
