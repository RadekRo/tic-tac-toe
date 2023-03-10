from board import display_board, get_empty_board, is_board_full, get_winning_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4

def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    current_player = "O"
    while is_game_running:
        display_board(board)
        ### TO DO ###
        # in each new iteration of the while loop the program should 
        # alternate the value of `current_player` from `X` to `O`
        match current_player:
            case "X":
                current_player = "O"
            case "O":
                current_player = "X"
        
        ### TO DO ###
        # based on the value of the variables `game_mode` and `current_player` 
        # the programm should should choose betwen the functions
        # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates
        match game_mode:
            case 1: #human vs human
                x, y = get_human_coordinates(board, current_player)
            case 2: #ai vs ai
                x, y = get_random_ai_coordinates(board, current_player)
            case 3: #human vs random ai
                if current_player == "X":
                    x, y = get_human_coordinates(board, current_player)
                else: 
                    x, y = get_random_ai_coordinates(board, current_player)
            case 4: #human vs unbeatable ai
                if current_player == "X":
                    x, y = get_human_coordinates(board, current_player)
                else:
                    x, y = get_unbeatable_ai_coordinates(board, current_player)
       
        board[x][y] = current_player
        
        ### TO DO ###
        # based on the values of `winning_player` and `its_a_tie` the program
        # should either stop displaying a winning/tie message 
        # OR continue the while loop
        winning_player = get_winning_player(board)
        its_a_tie = is_board_full(board)

        if its_a_tie:
            display_board(board)
            print("GAME OVER. It's a tie!")
            break
        if winning_player == "X" or winning_player == "O":
            display_board(board)
            print(f"GAME OVER. Player {winning_player} wins!")
            break

if __name__ == "__main__":
    main()