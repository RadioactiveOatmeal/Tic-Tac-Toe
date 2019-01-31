def determine_winner(lst):

    for i in range(3):
        if lst[i][0] == lst[i][1] == lst[i][2] == 'x':  # check horizontals for x
            print("Player 1 wins")
            return 1
        elif lst[i][0] == lst[i][1] == lst[i][2] == 'o':  # check horizontals for o
            print("Player 2 wins")
            return 1

    for i in range(3):
        if lst[0][i] == lst[1][i] == lst[2][i] == 'x':  # check verticals for x
            print("Player 1 wins")
            return 1
        elif lst[0][i] == lst[1][i] == lst[2][i] == 'o':  # check verticals for o
            print("Player 2 wins")
            return 1

    if lst[0][0] == lst[1][1] == lst[2][2] == 'x':  # check left top to right bottom diagonal for x
        print("Player 1 wins")
        return 1
    elif lst[0][0] == lst[1][1] == lst[2][2] == 'o':  # check left top to right bottom diagonal for o
        print("Player 2 wins")
        return 1
    if lst[2][0] == lst[1][1] == lst[0][2] == 'x':  # check left bottom to right top diagonal for x
        print("Player 1 wins")
        return 1
    if lst[2][0] == lst[1][1] == lst[0][2] == 'o':  # check left bottom to right top diagonal for o
        print("Player 2 wins")
        return 1
