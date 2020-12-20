from itertools import combinations

def solution(numbers, target):

    answer = 0

    # 모든 원소의 값의 합(모두 양의 부호(+)인 경우)에서 조합별 경우의 수를 빼주는(-) 방식을 사용할 예정.
    sum_numbers = sum(numbers)

    # 모든 원소의 값의 합이 타겟넘버인 경우. 타겟넘버를 만드는 방법은 오로지 하나.
    if sum_numbers == target:
        answer = 1

    else:
        # '음의 부호(-)'의 개수와 위치를 적용할 모든 조합의 수를 도출
        combinations_list = []
        for i in range(len(numbers)):
            combinations_list.append(list(combinations(numbers, i + 1)))

        # 각 조합길이 리스트별로 각 조합의 합(=음의 부호끼리 더해줌)을 도출
        sum_combinations_list = []
        for c_length in combinations_list:
            sum_list = list(map(sum, c_length))
            sum_list = sorted(sum_list)   # sorted 1번을 통하여, 아래의 max,min 각각 1번 돌리는 것을 대체.
            sum_combinations_list.append(sum_list)

        # 모든 원소의 값의 합(모두 양의 부호(+)인 경우)에서 각 조합의 합(=음의 부호끼리 더해줌)을 빼줘서 타겟넘버 도출
        for minus_list in sum_combinations_list:
            # 조합길이리스트에서 최대값을 빼줘도 타겟넘버보다 크거나, 최소값을 빼줘도 타겟넘버보다 작은 경우는 탐색 불필요
            if sum_numbers - 2 * (minus_list[len(minus_list) - 1]) > target or sum_numbers - 2 * (minus_list[0]) < target:
                continue
            else:
                answer += minus_list.count((sum_numbers - target) / 2)   # 방정식에 따라 타겟넘버가 나오는 숫자 도출하여, 개수 헤아림.

    return answer
