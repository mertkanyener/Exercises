import check_tic_tac_toe


def make_move(player, game):
    coords = input('Please enter the coordinates of your move in row,col form')
    move = coords.split(',')
    if game[int(move[0])][int(move[1])] == 0:
        if player == 1:
            game[int(move[0])][int(move[1])] = 'X'
            return True
        else:
            game[int(move[0])][int(move[1])] = 'O'
            return True
    else:
        print('Invalid move, try again')
        return False


def draw():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    current_player = 1
    free_square = 9
    p1_played = 0
    p2_played = 0
    while free_square != 0:
        if p1_played >= 3 or p2_played >= 3:
            if check_tic_tac_toe(game):
                break
        while current_player == 1:
            if make_move(current_player, game):
                current_player = 2
                p1_played += 1
                free_square += 1
        while current_player == 2:
            if make_move(current_player, game):
                current_player = 1
                p2_played += 1
                free_square += 1



