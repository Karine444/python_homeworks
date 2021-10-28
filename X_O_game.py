board = list(range(1, 10))

wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
'''
Since the winning combinations will be unchanged,
we will write all the possible options
'''


def draw_board():
    print("-----------")
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3])
    print("-----------")

'''
Draw a board for the game
'''

def take_input(player_token):
    while True:
        value = input(f'Where to put: {player_token} ?  ')
        if not (value in '123456789'):
            print('Enter one of these numbers(1,2,3,4,5,6,7,8,9)')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('This cage is already occupied')
            continue
        board[value - 1] = player_token
        break
'''If what the player wrote does not match the numbers on the plate, the player is asked again,
or if the cell is already occupied the player is asked again'''

def check_win():
    for i in wins_coord:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            text = board[i[1] - 1]
            return text
    else:
        return False

'''We refer to each number in each tuple by its index.If the characters in the tuples match then returns True'''

def play():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'You win!!')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Game Drawn!')
            break


'''if the "counter" is even, then the player bets 'X',and if not then 'O'.Then we check if all cells are occupied,
if yes then a draw
'''

play()

while True:
    # Player choice Menu
    print("Enter 1 , if you want to start the game again.")
    print("Enter 2 to Quit")
    # Try exception for CHOICE input
    try:
        choice = int(input("Your choice(1 or 2)?"))
    except ValueError:
        print("Wrong Input!!! Try Again\n")
        continue
    if choice == 1:
        play()
    elif choice == 2:
        break
    else:
        print("Wrong Choice!!!! Try Again\n")