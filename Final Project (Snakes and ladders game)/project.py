from pyfiglet import Figlet
from termcolor import colored
import random
import sys


def main():
    title = Figlet(font="slant", width=90)
    print(colored(title.renderText("SNAKES AND LADDERS") , "green"))
    name1 = input(colored("Enter Player 1 name: ", "cyan"))
    name2 = input(colored("Enter Player 2 name: ", "cyan"))

    while True:
        color1 = input(colored(f"Select a game token colour (red , green , yellow , blue , white) for {name1}: ", "green")).lower().strip()
        player1 = character(color1)
        if player1 == None:
            print("Invalid color")
        else:
            break
    while True:
        color2 = input(colored(f"Select a game token colour (red , green , yellow , blue , white) for {name2}: ", "green")).lower().strip()
        player2 = character(color2)
        if player2 == None:
            print("Invalid color")
        else:
             break
    d_1 = 1
    d_2 = 1
    while True:
        try:
            d_1 , d_2 , board = draw_map(player1, d_1 , name1, player2, d_2 , name2)
            borders(board)
            choice = input(colored(f"{name1}'s turn (Press Enter to roll the dice 🎲...) or type 'quit' to exit: ", color1)).lower().strip()
            if choice == "quit" or choice == "exit": 
                sys.exit("GoodBye")
            d1 = dice()
            print(colored(f"{name1}'s rolled: {d1}", color1))
            d_1 = d_1 + d1
            choice = input(colored(f"{name2}'s turn (Press Enter to roll the dice 🎲...) or type 'quit' to exit: ", color2)).lower().strip()
            if choice == "quit" or choice == "exit": 
                sys.exit("GoodBye")            
            d2 = dice()
            print(colored(f"{name2}'s rolled: {d2}", color2))
            d_2 = d_2 + d2
            input("Press Enter to continue...")
        except EOFError:
                sys.exit("GoodBye")



def dice():
    num = random.randint(1, 6)
    return num


def draw_map(p1, pos1, name1, p2, pos2 , name2 ):
    board = [
        ["  31  ", "  🐍  ", "  33  ", "  🐍  ", "  35  ", "  🚩   "],
        ["  🪜   ", "  26  ", "  27  ", "  28  ", "  🐍  ", "  30  "],
        ["  19  ", "  20  ", "  🐍  ", "  22  ", "  23  ", "  24  "],
        ["  🪜   ", "  14  ", "  15  ", "  16  ", "  🪜   ", "  18  "],
        ["  7   ", "  🐍  ", "  9   ", "  10  ", "  11  ", "  12  "],
        ["  1   ", "  2   ", "  3   ", "  🪜   ", "  5   ", "  6   "],
    ]

    if (pos1 // 6 == 0):
        ps1 = pos1 % 6
        if board[5][ps1 - 1] == "  🪜   ":
            board[4][ps1 - 1] = p1
            pos1 += 6
            print(f"That 🪜  just adopted {name1}. Enjoy the free ride!")
        else:
            board[5][(ps1) - 1] = p1
    elif pos1 == 6:
            board[5][5] = p1
    elif (pos1 // 6 == 1):
        ps1 = pos1 % 6
        if board[4][ps1 - 1] == "  🐍  ":
            board[5][ps1 - 1] = p1
            pos1 -= 6
            print(f"A 🐍  dragged {name1} down")
        else:
            board[4][(ps1) - 1] = p1
    elif pos1 == 12:
            board[4][5] = p1
    elif pos1 // 6 == 2:
        ps1 = pos1 % 6
        if board[3][ps1 - 1] == "  🪜   ":
            board[2][ps1 - 1] = p1
            pos1 += 6
            print(f"That 🪜  just adopted {name1}. Enjoy the free ride!")
        else:
            board[3][(ps1) - 1] = p1
    elif pos1 == 18:
            board[3][5] = p1
    elif pos1 // 6 == 3:
        ps1 = pos1 % 6
        if board[2][ps1 - 1] == "  🐍  ":
            board[3][ps1 - 1] = p1
            pos1 -= 6
            print(f"A 🐍  dragged {name1} down")
        else:
            board[2][(ps1) - 1] = p1
    elif pos1 == 24:
            board[2][5] = p1    
    elif pos1 // 6 == 4:
        ps1 = pos1 % 6
        if board[1][ps1 - 1] == "  🪜   ":
            board[0][ps1 - 1] = p1
            pos1 += 6
            print(f"That 🪜  just adopted {name1}. Enjoy the free ride!")
        elif board[1][ps1 - 1] == "  🐍  ":
            board[2][ps1 - 1] = p1
            pos1 -= 6
            print(f"A 🐍  dragged {name1} down")
        else:
            board[1][(ps1) - 1] = p1
    elif pos1 == 30:
            board[1][5] = p1
    elif pos1 // 6 == 5:
        ps1 = pos1 % 6
        if board[0][ps1 - 1] == "  🐍  ":
            board[1][ps1 - 1] = p1
            pos1 -= 6
            print(f"A 🐍  dragged {name1} down")
        else:
            board[0][(ps1) - 1] = p1
    else:
        sys.exit(colored(f"Congratulations to {name1}", "red"))


    if pos2 // 6 == 0 :
        ps2 = pos2 % 6
        if board[5][ps2 - 1] == "  🪜   ":
            board[4][ps2 - 1] = p2
            pos2 += 6
            print(f"That 🪜  just adopted {name2}. Enjoy the free ride!")
        else:
            board[5][(ps2) - 1] = p2
    elif pos2 == 6:
            board[5][5] = p2
    elif pos2 // 6 == 1 :
        ps2 = pos2 % 6
        if board[4][ps2 - 1] == "  🐍  ":
            board[5][ps2 - 1] = p2
            pos2 -= 6
            print(f"A 🐍  dragged {name2} down")
        else:
            board[4][(ps2) - 1] = p2
    elif pos2 == 12:
            board[4][5] = p2
    elif pos2 // 6 == 2:
        ps2 = pos2 % 6
        if board[3][ps2 - 1] == "  🪜   ":
            board[2][ps2 - 1] = p2
            pos2 += 6
            print(f"That 🪜  just adopted {name2}. Enjoy the free ride!")
        else:
            board[3][(ps2) - 1] = p2
    elif pos2 == 18:
            board[3][5] = p2
    elif pos2 // 6 == 3 :
        ps2 = pos2 % 6
        if board[2][ps2 - 1] == "  🐍  ":
            board[3][ps2 - 1] = p2
            pos2 -= 6
            print(f"A 🐍  dragged {name2} down")
        else:
            board[2][(ps2) - 1] = p2
    elif pos2 == 24:
            board[2][5] = p2  
    elif pos2 // 6 == 4:
        ps2 = pos2 % 6
        if board[1][ps2 - 1] == "  🪜   ":
            board[0][ps2 - 1] = p2
            pos2 += 6
            print(f"That 🪜  just adopted {name2}. Enjoy the free ride!")
        elif board[1][ps2 - 1] == "  🐍  ":
            board[2][ps2 - 1] = p2
            pos2 -= 6
            print(f"A 🐍  dragged {name2} down")
        else:
            board[1][(ps2) - 1] = p2
    elif pos2 == 30:
            board[1][5] = p2
    elif pos2 // 6 == 5:
        ps2 = pos2 % 6
        if board[0][ps2 - 1] == "  🐍  ":
            board[1][ps2 - 1] = p2
            pos2 -= 6
            print(f"A 🐍  dragged {name2} down")
        else:
            board[0][(ps2) - 1] = p2
    else:
        sys.exit(colored(f"Congratulations to {name2}" , "yellow"))
    if pos1 == pos2 and pos1 <= 36:
        combined = f" {p1.strip()}{p2.strip()} "
        row = 5 - ((pos1 - 1) // 6)
        col = (pos1 - 1) % 6
        board[row][col] = combined
    return pos1 , pos2 , board


def character(colour):
    if colour == "red":
        return "  🟥  "
    elif colour == "blue":
        return "  🟦  "
    elif colour == "green":
        return "  🟩  "
    elif colour == "yellow":
        return "  🟨  "
    elif colour == "white":
        return "  ⬜  "
    return None


def borders(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 53)


if __name__ == "__main__":
    main()
