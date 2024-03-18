# Tic Tac Toe

This Python program allows you to play Tic Tac Toe against another player. Player 1 is represented by X, and Player 2 is represented by O. Let's play!

## How to Play

1. **Introduction**: 
    - When you start the game, you'll be welcomed to Tic Tac Toe and informed that Player 1 is X and Player 2 is O.

2. **Game Board**: 
    - The game board is a 3x3 grid, where each cell is numbered from 1 to 9. Players take turns placing their symbols (X or O) on the board.

3. **Printing the Board**:
    - The `print_board()` function prints the current state of the board after each move in a visually appealing format.

4. **Getting a Move**:
    - The `get_move()` function prompts the current player to enter a number corresponding to the cell where they want to place their symbol.

5. **Updating the Board**:
    - The `update_board()` function updates the board with the current player's move.

6. **Checking for a Winner**:
    - The `check_winner()` function checks if there's a winner after each move. It checks rows, columns, and diagonals for three consecutive symbols.

7. **Main Game Loop**:
    - The `main()` function initializes the game board and starts the main game loop. Players take turns making moves until there's a winner or a tie.

## Getting Started

To play Tic Tac Toe, simply run the `main()` function in the `tic_tac_toe.py` file. Follow the on-screen instructions to make your moves.

Example usage:

```bash
$ python tic_tac_toe.py
Welcome to Tic Tac Toe!
Player 1 is X and Player 2 is O. Let's play!
---+---+---
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
---+---+---
Player X, enter a number: 1
---+---+---
 X | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
---+---+---
...
```

## Running the Tests

To run the automated tests for this system, simply execute the `test_tic_tac_toe.py` file:

```bash
$ python test_tic_tac_toe.py
```

## Built With

- Python

## Authors

- [Inuk Baik](https://github.com/inukbaik)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---