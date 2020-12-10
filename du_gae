def solution(numbers):
    answer = []

    for i in list(combinations(numbers, 2)):   # 두 수의 조합
        answer.append(i[0] + i[1])

    return sorted(list(set(answer)))   # 중복제거 후, 다시 리스트로 바꿔주고, 정렬

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
