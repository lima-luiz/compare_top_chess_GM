import chess.pgn
import sys
import io

def read_csv_file(file):
    moves = []
    with open(file, "r") as f:
        data = f.read()
    moves_per_game = data.split("\n")
    for game in moves_per_game:
        white_moves = game.split(";")[-2].replace(" ","")
        black_moves = game.split(";")[-1].replace(" ","")
        moves.append([white_moves, black_moves])
    return moves


def board_by_list_of_moves(moves):
    current_moves = ""
    for game_id, game in enumerate(moves):
        white_moves = game[0].split(".")
        black_moves = game[1].split(".")
        total_moves = len(white_moves) + len(black_moves)
        index = 0
        while total_moves > 0:
            current_moves += str(index+1) + ". "
            current_moves += str(white_moves[index]) + " "
            total_moves -= 1
            try:
                current_moves += str(black_moves[index]) + " "
            except:
                break
            else:
                total_moves -= 1
                index += 1
        pgn = io.StringIO(current_moves)
        game = chess.pgn.read_game(pgn)
        if len(game.errors) > 0:
            print(game_id)
            print(current_moves)
            print(game.errors)
        current_moves = ""


def test_SQL_moves():
    file = sys.argv[1]
    moves = read_csv_file(file)
    board_by_list_of_moves(moves)


if __name__ == "__main__":
    test_SQL_moves()