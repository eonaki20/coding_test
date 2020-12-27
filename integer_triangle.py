def solution(triangle):

    # Base Case
    sum_list = []
    sum_list.append(triangle[0][0] + triangle[1][0])
    sum_list.append(triangle[0][0] + triangle[1][1])

    # 반복문 Case
    for i in range(2, len(triangle)):
        temp_list = sum_list   # 반복문에 사용할 임시의 합계리스트 생성
        sum_list = []   # 합계리스트 초기화
        sum_list.append(temp_list[0] + triangle[i][0])   # 맨왼쪽
        for j in range(1, i):   # 안쪽(둘 중 더 큰 숫자를 더함)
            sum_list.append(max(temp_list[j - 1] + triangle[i][j], temp_list[j] + triangle[i][j]))
        sum_list.append(temp_list[i - 1] + triangle[i][i])   # 맨오른쪽

    answer = max(sum_list)
    return answer
