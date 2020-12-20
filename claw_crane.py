def solution(board, moves):

    # 열(column) 단위로 인형 리스트 만듦
    board_col = []
    for i in range(len(board)):
        column = []
        for j in range(len(board)):
            column.append(board[j][i])
            while 0 in column:  # 인형이 없는 빈칸은 지워줌
                column.remove(0)
        board_col.append(column)

    basket = []  # 뽑은 인형을 넣을 바구니
    count = 0   # 겹쳐서 사라지는 인형의 개수

    # 인형뽑기 과정
    for i in moves:
        # '바구니'와 '뽑을 열'에 모두 인형이 있을 때
        if basket and board_col[i - 1]:
            if basket[len(basket) - 1] != board_col[i - 1][0]:
                basket.append(board_col[i - 1][0])
                del board_col[i - 1][0]
            else:  # 같은 모양의 인형 두 개가 연속하여 쌓이는 상황
                del basket[len(basket) - 1]
                del board_col[i - 1][0]
                count += 2

        # '바구니'에 인형이 없고, '뽑을 열'에 인형이 있을 때
        if not basket and board_col[i - 1]:
            basket.append(board_col[i - 1][0])
            del board_col[i - 1][0]

        # '뽑을 열'에 인형이 없을 때
        else:
            continue  # 다음 턴(move)으로 패스

    answer = count
    return answer
