# TODO a board of 3x3 suares
# TODO two players "x" and "o"
# TODO check if square is free or empty
# TODO if square is free, insert the sign of the player
# TODO check win
# TODO asks if another game

from tabulate import tabulate
import random


def starting_player():
    to_start = random.randint(0, 1)
    return to_start


def sign(to_start):
    if starting_player() == 1:
        player = "x"
    else:
        player = "0"
    return player


def is_free(scheme, a, i):
    return scheme[a][i] == ""


def switch(player):
    if player == "x":
        player = "0"
        return player
    else:
        player = "x"
        return player


def check_win(scheme, player):
    if (
        scheme[1][0] == scheme[2][0] == scheme[3][0]
        and scheme[1][0] != ""
        and scheme[1][0] == player
    ):
        return True
    elif (
        scheme[1][1] == scheme[2][1] == scheme[3][1]
        and scheme[2][0] != ""
        and scheme[2][0] == player
    ):
        return True
    elif (
        scheme[1][2] == scheme[2][2] == scheme[3][2]
        and scheme[3][0] != ""
        and scheme[3][0] == player
    ):
        return True
    elif (
        scheme[1][0] == scheme[1][1] == scheme[1][2]
        and scheme[1][0] != ""
        and scheme[1][0] == player
    ):
        return True
    elif (
        scheme[2][0] == scheme[2][1] == scheme[2][2]
        and scheme[2][0] != ""
        and scheme[2][0] == player
    ):
        return True
    elif (
        scheme[3][0] == scheme[3][1] == scheme[3][2]
        and scheme[3][0] != ""
        and scheme[3][0] == player
    ):
        return True
    elif (
        scheme[1][0] == scheme[2][1] == scheme[3][2]
        and scheme[1][0] != ""
        and scheme[1][0] == player
    ):
        return True
    elif (
        scheme[1][2] == scheme[2][1] == scheme[3][0]
        and scheme[1][2] != ""
        and scheme[1][2] == player
    ):
        return True
    else:
        return False


def fullBoard(scheme):
    keys = [1, 2, 3]
    values = list(map(scheme.get, keys))
    final = [*values[0], *values[1], *values[2]]
    if not "" in final:
        return True


def play():
    scheme = {1: ["", "", ""], 2: ["", "", ""], 3: ["", "", ""]}
    board = tabulate(scheme, tablefmt="grid")
    print(board)
    player = sign(starting_player)
    print(f"The game starts player {player}")
    while True:

        a = int(input("Enter column [1,2,3]: "))
        i = int(input("Enter position [0,1,2]: "))
        if is_free(scheme, a, i):
            scheme[a][i] = player
            board = tabulate(scheme, tablefmt="grid")
            if check_win(scheme, player):
                print(board)
                print(f"Great, player {player} won!")
                break
            if fullBoard(scheme):
                print(board)
                print("You end up tie!")
                break
            player = switch(player)
            print(board)
            print(scheme)
            print(f"Player {player} to move!")
        else:
            print("Please try again with valid column(1,2,3) and position(0,1,2)")
            print(board)


def main():
    play()


if __name__ == "__main__":
    main()
