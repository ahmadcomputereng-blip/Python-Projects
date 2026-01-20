# Snakes and Ladders
#### Video Demo:  <https://youtu.be/-14p_l6pO_s?si=mCZhkAwlDN_OBsls>
#### Description:

This is a terminal-based implementation of the classic board game **Snakes and Ladders**, developed as my final project for CS50P.

The project uses Python to simulate the game logic and creates a visual representation of the board in the command line. It leverages external libraries to enhance the user interface:
- **`pyfiglet`**: Renders the "SNAKES AND LADDERS" title in stylised ASCII art.
- **`termcolor`**: Adds color to the text, tokens, and board elements to differentiate between players and game events.

### Features
1.  **Dynamic Board**: The board is a 6x6 grid (36 squares) that updates visually after every turn.
2.  **Customizable Players**: Two players can enter their names and choose their token colors (Red, Blue, Green, Yellow, or White).
3.  **Input Validation**: The game ensures players select valid colors and handles errors gracefully.
4.  **Game Logic**:
    - **Ladders (🪜)**: If a player lands on a ladder, they move up to a higher square.
    - **Snakes (🐍)**: If a player lands on a snake head, they slide down to a lower square.
    - **Collision Handling**: If both players land on the same square, the board displays both tokens side-by-side.
5.  **Winning Condition**: The first player to reach square 36 (or higher) wins the game.

### Project Files
- `project.py`: Contains the main game loop, the logic for drawing the map, and the functions for dice rolling and movement.
- `test_project.py`: Contains unit tests for the game functions using `pytest`.
- `requirements.txt`: Lists the external libraries required to run the project.

### How to Run
1.  Install the dependencies: `pip install -r requirements.txt`
2.  Run the game: `python project.py`
