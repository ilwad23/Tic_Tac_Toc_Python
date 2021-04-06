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
        turn('X')
        turn('O')
        if (check_game() == True):
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
    # if the game is still going then the next player can take their turn
    if (check_game() == False or check_game() == False):
        move = decided_move(player)
        os.system('clear')
        borad[move] = player
        display_borad()
        return 
def decided_move(player):
    # this function receives the player chosen position and validated their input
    while True:
        try:
            choice = input(f'Choose a positon between 1-9, {player}: ').strip()
            if (borad[int(choice)-1] == ' ' and choice != '0'): return int(choice)-1
        except: continue
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
def check_each(combination):
    global winner
    # checks all of †he winning combinations by seeing if there three of the same letter
    check_winner = combination.count(combination[0]) == 3 and combination[0] != ' '
    # variable will contain winner - X or O
    winner = combination[0] if check_winner else ''
    return check_winner
#======================================================================================
#  start game
game()
