from pprint import pprint
from win import determine_winner

board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

pprint(board, width='17')

for turn in range(9):

    while True:  # check if the spot is already used
        temp = input("\nPlayer 1: enter values\n")
        temp_list = list(temp)
        if board[int(temp_list[0])][int(temp_list[1])] != '-':
            continue
        else:
            break

    del board[int(temp_list[0])][int(temp_list[1])]   # delete position that was entered and replace it with an x
    board[int(temp_list[0])].insert(int(temp_list[1]), 'x')
    pprint(board, width=17)

    if determine_winner(board) == 1:
        break

    while True:  # check if the spot is already used
        temp2 = input("\nPlayer 2: enter values\n")
        temp_list2 = list(temp2)
        if board[int(temp_list2[0])][int(temp_list2[1])] != '-':
            continue
        else:
            break

    del board[int(temp_list2[0])][int(temp_list2[1])]  # delete position that was entered and replace it with an o
    board[int(temp_list2[0])].insert(int(temp_list2[1]), 'o')
    pprint(board, width=17)

    if determine_winner(board) == 1:
        break

if determine_winner(board) != 1:
    print("a draw!")
