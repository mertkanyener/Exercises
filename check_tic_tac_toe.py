def line_match(table):
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2]:
            return table[i][0]
    return 0


def column_match(table):
    for i in range(3):
        if table[0][i] == table[1][i] == table[2][i]:
            return table[0][i]
    return 0

def diagonal_match(table):
    if table[0][0] == table[1][1] == table[2][2]:
        return table[0][0]
    elif table[0][2] == table[1][1] == table[2][0]:
        return table[0][2]
    else:
        return 0


def check_winner(table):
    if line_match(table) > 0:
        print('The winner is player' + str(line_match(table)))
        return True
    elif column_match(table) > 0:
        print('The winner is player' + str(column_match(table)))
        return True
    elif diagonal_match(table) > 0:
        print('The winner is player' + str(diagonal_match(table)))
        return True
    else:
        print("There's no winner")
        return False


game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	                [2, 1, 0],
	                [2, 1, 1]]

no_winner = [[1, 2, 0],
	         [2, 1, 0],
	         [2, 1, 2]]

also_no_winner = [[1, 2, 0],
	              [2, 1, 0],
	              [2, 1, 0]]

"""check_winner(game)
check_winner(winner_is_1)
check_winner(winner_is_2)
check_winner(winner_is_also_1)
check_winner(no_winner)
check_winner(also_no_winner)
"""