def solution(phone_book):

    '''전화번호와 전화번호길이를 key-value로 묶어서 활용'''
    dic_phone_book = {}

    len_phone_number = list(map(len, phone_book))

    # print(len_phone_number)

    for i in range(len(phone_book)):
        dic_phone_book[phone_book[i]] = len_phone_number[i]

    '''전화번호길이를 기준으로 정렬'''
    sorted_dic_phone_book = sorted(dic_phone_book.items(), key=lambda x: x[1])

    for i in range(len(sorted_dic_phone_book) - 1):
        for j in range(i + 1, len(sorted_dic_phone_book)):
            if sorted_dic_phone_book[i][0] != sorted_dic_phone_book[j][0][:sorted_dic_phone_book[i][1]]:
                pass
            else:
                return False
    return True
