import random

class SudokuBoard:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def set_cell(self, row, col, value):
        if 0 <= row < 9 and 0 <= col < 9 and 0 <= value <= 9:
            self.grid[row][col] = value
            return True
        return False

    def get_cell(self, row, col):
        if 0 <= row < 9 and 0 <= col < 9:
            return self.grid[row][col]
        return None

    def is_valid_move(self, row, col, value):
        if value == 0:
            return True
        for i in range(9):
            if i != col and self.grid[row][i] == value:
                return False
        for i in range(9):
            if i != row and self.grid[i][col] == value:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if (i != row or j != col) and self.grid[i][j] == value:
                    return False
        return True

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "
            cell = board.get_cell(i, j)
            row += (str(cell) if cell != 0 else ".") + " "
        print(row)

def generate_random_puzzle(board, num_clues=30):
    attempts = 0
    placed = 0
    max_attempts = num_clues * 10
    while placed < num_clues and attempts < max_attempts:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        value = random.randint(1, 9)
        if board.get_cell(row, col) == 0 and board.is_valid_move(row, col, value):
            board.set_cell(row, col, value)
            placed += 1
        attempts += 1
    return placed == num_clues

def manual_input(board):
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()
            if len(lines) != 9:
                print(f"Error: input.txt must contain exactly 9 rows, found {len(lines)}.")
                return False
            for row, line in enumerate(lines):
                values = line.strip().split()
                if len(values) != 9:
                    print(f"Error: Row {row + 1} must contain exactly 9 values, found {len(values)}.")
                    return False
                row_values = []
                for val in values:
                    if val == ".":
                        row_values.append(0)
                    elif val.isdigit() and 1 <= int(val) <= 9:
                        row_values.append(int(val))
                    else:
                        print(f"Error: Invalid value '{val}' in Row {row + 1}. Use '.' or 1-9.")
                        return False
                for col, value in enumerate(row_values):
                    board.set_cell(row, col, value)
        print("\nPuzzle read successfully.")
        return True
    except FileNotFoundError:
        print("Error: input.txt not found in the current directory.")
        return False
    except Exception as e:
        print(f"Error reading input.txt: {str(e)}")
        return False

def main():
    print("Sudoku Puzzle")
    print("1. Manual Input")
    print("2. Auto-Generate Puzzle")
    choice = input("Choose an option (1 or 2): ").strip()
    board = SudokuBoard()
    if choice == "1":
        print("\nManual Input Mode")
        if not manual_input(board):
            print("Failed to load puzzle from input.txt.")
    elif choice == "2":
        print("\nAuto-Generate Puzzle Mode")
        if not generate_random_puzzle(board, num_clues=30):
            print("Failed to generate puzzle with 30 clues.")
    else:
        print("Invalid choice. Exiting.")
        return
    print("\nGenerated Puzzle:")
    print_board(board)

if __name__ == "__main__":
    main()

