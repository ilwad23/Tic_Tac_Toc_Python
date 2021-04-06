import os
os.system('clear')
#======================================================================================
# variables
borad = [' ']*9
winner = ''
#======================================================================================
# the following functions - plays and displays the game        
def game():
    display_borad()
    # the while loop will keep on till there a winner and tie  
    while True:
        # human player's turn 
        turn('X')
        # computer player's turn 
        turn('O')
        # checking the status the game and whether it is over
        if (check_game()):
            # the winner can be - 'X', 'O' or 'no one'
            print(winner, 'won')
            break
def display_borad():
    b = borad
    print(' - | - | -')
    for p in range(3):
        print(f' {b[3*p]} | {b[3*p+1]} | {b[3*p+2]}\n - | - | - ')
#======================================================================================
# the following functions - gets the input of the players, validates it and then displays it.
def turn(player):
    # if the game is still going then the next player can take their turn and their move will be display to them
    if (not check_game()):
        move = decided_move(player)
        os.system('clear')
        borad[move] = player
        if player == 'O': display_borad()
        return 
def decided_move(player):
    # the block below receives the computer player 
    if player == 'O':
        return best_spot(borad)
    # the block below receives the human player chosen move and validated their input
    if player == 'X':
        while True:
            try:
                choice = input(f'Choose a positon between 1-9, {player}: ').strip()
                if (borad[int(choice)-1] == ' ' and choice != '0'):
                    return int(choice)-1
            except:
                continue
#======================================================================================
# the following functions - will find the best spot for the computer player
def best_spot(borad):
    # this function will return the index for the best spot by using minimax algorithm
    global winner
    best_score, best_index = -1000,None
    for i, j in enumerate(borad):
        if j == ' ':
            borad[i] = 'O'
            s = minimax(borad,False)
            borad[i], winner = ' ', ''
            if best_score < s:
                best_score, best_index = s, i
    print(check_game())
    return best_index
def minimax(borad, player):
    # 'A minimax algorithm is a recursive algorithm for choosing the next move in an n-player game, usually a two-player game. A value is associated with each move or state of the game.' ~ Wikipedia
    global winner
    # checking whether the move cause a win or a tie and  then return an appropriate score
    score = {'X':-1,'O':1,'no one':0}
    if check_game():
        return score[winner]    
    # if there is no score then the next player will be positioned in the next empty spot and the algorithm will be called again 
    best_score = -1000 if player else 1000
    for i, j in enumerate(borad):
        if j == ' ':
            borad[i] = 'O' if player else 'X'
            score = minimax(borad, not player)
            borad[i], winner = ' ', ''
            min_max = max if player else min
            best_score = min_max(score, best_score)
    return best_score
#======================================================================================
# the following functions - will check the status of the game to see if there is a winner or tie
def check_game():
    global winner
    for k in range(3):
        # check rows 
        if  (check_each([borad[(3*k)+i] for i in range(3)])): return True
        # check columns
        if  (check_each([borad[(3*i)+k] for i in range(3)])): return True
    # check left diagonal
    if  (check_each([borad[i*3+i] for i in range(3)])): return True
    # check right diagonal
    if  (check_each([borad[i*3+(2-i)] for i in range(3)])): return True
    # check tie
    if not (' ' in borad):
        winner = 'no one' 
        return True
    return False
def check_each(listOfStrings):
    global winner
    # checks all of †he winning combinations by seeing if there three of the same letter
    check_winner = listOfStrings.count(listOfStrings[0]) == 3 and listOfStrings[0] != ' '
    # variable will contain winner - X or O
    winner = listOfStrings[0] if check_winner else ''
    return check_winner
#======================================================================================
# start game
game()
