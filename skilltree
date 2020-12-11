''' solve_1(28.6/100) -> 100/100(선행스킬순서와 무관한 스킬들로만 이루어진 경우까지 고려하였더니 정답이 됨~)'''
def solution(skill, skill_trees):
    answer = 0

    # 가능한 스킬트리 리스트 작성
    possible_skill_list = []
    for i in range(len(skill) + 1):
        possible_skill_list.append(skill[0:i])   # skill = "CBD"의 경우, '', 'C','CB','CBD'가 가능한 스킬트리.
    '''위의 가능한 스킬트리 경우의 수 중 ''는 선행스킬순서와 무관한 스킬들로만 이루어진 경우에 해당함.'''

    # skill_trees의 원소들을 하나씩 가능한 스킬트리 리스트에 포함되는지 확인
    for element in skill_trees:
        skill_list = []   # 바로 문자열로 만들어주는 방법을 모르겠으니 일단 리스트의 원소로 넣어준 후, 문자열로 환원하는 방식 사용
        for a in element:   # 원소의 문자열을 하나씩 확인
            if a in skill:
                skill_list.append(a)   # 선행스킬순서와 관련있는 문자(스킬)만 확인 대상. 선행스킬순서와 무관한 스킬은 제외.
        str_skill_list = "".join(map(str, skill_list))   # 공백없이 원소들을 문자열(string)으로 환원. 원소들이 str타입이므로 타입변환 불필요.
        if str_skill_list in possible_skill_list:
            answer += 1
    return answer
