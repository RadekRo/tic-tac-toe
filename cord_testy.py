from board import display_board, get_empty_board, is_board_full, get_winning_player
import random
current_player = ""
def get_human_coordinates(board, current_player):
    alphabet_to_index = {'A': 0, 'B': 1, 'C': 2}
    numbers_to_index = {'1': 0, '2': 1, '3': 2}
    alphabet_valid = ["C", "B", "A"]
    numbers_valid = ["1", "2", "3"]
    while True:
        move_pos = input("Please enter your move: ")
        move_pos = move_pos.upper()
        if move_pos != "" and len(move_pos) == 2:
            row = list(move_pos)[0]
            col = list(move_pos)[1]
            if row in alphabet_valid and col in numbers_valid and board[alphabet_to_index[row]][numbers_to_index[col]] == ".":
                match row:
                  case "A":
                    row = 0
                  case "B":
                    row = 1
                  case "C":
                    row = 3
                return int(row), int(col)-1
            else:
                print("This position is taken.")
        else:
            print("Please enter a valid position! A-C, 1-3")


def get_random_ai_coordinates(board, current_player):
    """
    Should return a tuple of 2 numbers.
    Each number should be between 0-2.
    The chosen number should be only a free coordinate from the board.
    If the board is full (all spots taken by either X or O) than "None"
    should be returned.
    """
    """Returns the coordinates of a valid move for player on board."""
    while True:
        row = random.randrange(len(board))
        col = random.randrange(len(board[row]))
        if board[row][col] == '.':
            break
    return row, col

def get_unbeatable_ai_coordinates(board, current_player):
  pass

if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2, current_player))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2, current_player))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2, current_player))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3, current_player))



  # board_4 = [
  #   [".", "O", "."],
  #   ["X", "O", "."],
  #   ["X", "X", "O"],
  # ]
  # print("The printed coordinate should always be (0, 0)")
  # print(get_unbeatable_ai_coordinates(board_4, "X"))
  #
  # board_5 = [
  #   ["X", "O", "."],
  #   ["X", ".", "."],
  #   ["O", "O", "X"],
  # ]
  # print("The printed coordinate should always be (1, 1)")
  # print(get_unbeatable_ai_coordinates(board_5, "O"))
  #
  # board_6 = [
  #   ["O", "O", "."],
  #   ["O", "X", "."],
  #   [".", "X", "."],
  # ]
  # print("The printed coordinate should either (0, 2) or (2, 0)")
  # print(get_unbeatable_ai_coordinates(board_6))