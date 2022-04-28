'''
Tic_Tac_Toe
by Brendon Hamson
'''

def main():
    board = create_board()
    player = current_player("")
    while not (get_winner(board) or get_a_draw(board)):
        show_board(board)
        make_move(player, board)
        player = current_player(player)
        if get_winner(board) == True:
            print(" ------ THREE IN A ROW!!! ------ ")
            print(" Great Job. Thank you for playing")
            print()
    show_board(board)
    print("Thank you for playing")
    print()



def create_board():
    board = []
    for spot in range(9):
        board.append(spot + 1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def get_a_draw(board):
    for spot in range(9):
        if board[spot] != "x" and board[spot] != "o":
            return False
    return True 
    
def get_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def current_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()