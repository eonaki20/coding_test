def solution(clothes):

    '''key(의상의 종류)-value(종류별 개수)'''

    clothes_type = {}

    for piece in clothes:
        if piece[1] not in clothes_type:
            clothes_type[piece[1]] = 1
        else:
            clothes_type[piece[1]] += 1

    number_of_cases = 1
    for cases in clothes_type.values():
        number_of_cases *= (cases + 1)

    return number_of_cases - 1
