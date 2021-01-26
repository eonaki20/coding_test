from collections import deque

def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)
    trucks_on = deque([])
    trucks_on_check = deque([])

    trucks_on.append(truck_weights[0])
    sum_weights = truck_weights[0]
    truck_weights.popleft()
    sec_count = 1
    trucks_on_check.append(sec_count)

    while truck_weights:
        if sum_weights + truck_weights[0] <= weight:
            trucks_on.append(truck_weights[0])
            sum_weights += truck_weights[0]
            truck_weights.popleft()
            sec_count += 1
            trucks_on_check.append(sec_count)
            if trucks_on_check[0] + (bridge_length - 1) == sec_count:
                sum_weights -= trucks_on[0]
                trucks_on.popleft()
                trucks_on_check.popleft()
        else:
            sec_count += 1
            if trucks_on_check[0] + (bridge_length - 1) == sec_count:
                sum_weights -= trucks_on[0]
                trucks_on.popleft()
                trucks_on_check.popleft()

    return sec_count + bridge_length
