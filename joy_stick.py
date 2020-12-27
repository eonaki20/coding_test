def solution(name):
    # 파이썬 모듈 활용
    from string import ascii_uppercase
    alhpa_list = list(ascii_uppercase)  # 알파벳 대문자 리스트

    up_or_down_count = 0  # 커서 위,아래 조작횟수
    right_or_left_count = 0  # 커서 위,아래 조작횟수

    up_or_down = {}  # 알파벳(key)과 각 알파벳의 커서 조작횟수(value)
    for i in range(len(alhpa_list) // 2 + 1):
        up_or_down[alhpa_list[i]] = i
    for i in range(len(alhpa_list) // 2 + 1, len(alhpa_list)):
        up_or_down[alhpa_list[i]] = len(alhpa_list) - i
    # print(up_or_down)

    # "A"를 제외한 나머지 알파벳의 위치정보 리스트 작성
    location_list = []
    for i in range(len(name)):
        if name[i] != "A":
            location_list.append(i)
        else:
            continue

    # name이 모두 "A"로만 이루어진 경우(아래 3줄의 코드가 없을 겅우, 리스트 범위 오류 발생)
    if location_list == []:
        answer = 0
        return answer

    # "A"를 제외한 나머지 알파벳의 위,아래 조작횟수의 합
    for not_a in location_list:
        up_or_down_count += up_or_down[name[not_a]]
    # print(up_or_down_count)

    present = 0  # 커서현재위치 기초값: 첫번째 위치

    if location_list[0] == 0:  # name의 첫 알파벳이 "A"가 아닐 경우, 위치정보를 삭제.
        del location_list[0]  # 좌우 커서 이동 시, 이동 전의 현재위치정보를 삭제함. 다음에 도착지점으로 지정되지 않도록 하기 위함.

    # '커서현재위치'와 '다음 "A"를 제외한 나머지 알파벳의 상대위치'와의 거리에 따라서 오른쪽으로 이동할지, 왼쪽으로 이동할지 결정
    while len(location_list) > 0:  # 좌우 커서 이동 전의 현재위치가 모두 삭제되면, 모든 좌우 이동 종료.
        if present < min(location_list):  # '커서현재위치'가 '다른 "A"를 제외한 나머지 알파벳들'보다 왼편일때
            if location_list[0] - present <= present + (len(name) - location_list[len(location_list) - 1]):
                right_or_left_count += location_list[0] - present
                present = location_list[0]
                del location_list[0]
            else:
                right_or_left_count += present + (len(name) - location_list[len(location_list) - 1])
                present = location_list[len(location_list) - 1]
                del location_list[len(location_list) - 1]
        else:  # '커서현재위치'가 '다른 "A"를 제외한 나머지 알파벳들'보다 오른편일때
            if present - location_list[len(location_list) - 1] <= (len(name) - present) + location_list[0]:
                right_or_left_count += present - location_list[len(location_list) - 1]
                present = location_list[len(location_list) - 1]
                del location_list[len(location_list) - 1]
            else:
                right_or_left_count += (len(name) - present) + location_list[0]
                present = location_list[0]
                del location_list[0]

    # print(right_or_left_count)

    # 위아래 커서 조작횟수 합 + 좌우 커서 조작횟수 합
    answer = up_or_down_count + right_or_left_count

    return answer

print(solution("JAN"))   #23
print(solution("JEROEN"))   #56
print(solution("AAA"))   #0
print(solution("BBBAAAB"))   #9
print(solution("ABABAAAAABA"))   #11
