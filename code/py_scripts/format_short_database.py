import sys
import os


def read_file_contents(file_path):
    with open(file_path, "r") as f:
        short_database_gross = f.read()
    return short_database_gross


def clean_short_database(short_database_gross):
    actions = [clean_event, clean_site, clean_date, clean_round, clean_white, clean_black, clean_result,
               clean_rating, clean_rating, clean_ECO]
    short_database_gross = short_database_gross.split("\n")
    short_database_clean = []
    for index, game in enumerate(short_database_gross):
        current_game_clean = []
        info = game.split(";")
        for index2, item in enumerate(info[:-1]):
            current_game_clean.append(actions[index2](item))
        moves_white, moves_black = clean_moves(info[-1])
        current_game_clean.append(moves_white)
        current_game_clean.append(moves_black)
        short_database_clean.append(current_game_clean)
        print(index)
    return short_database_clean


def clean_event(event_info):
    event_info = event_info.replace("[Event ","")
    event_info = event_info.replace("]", "")
    event_info = event_info.replace('"', '')
    return event_info


def clean_site(site_info):
    site_info = site_info.replace("[Site ", "")
    site_info = site_info.replace("]", "")
    site_info = site_info.replace('"', '')
    return site_info


def clean_date(date_info):
    date_info = date_info.replace("[Date ", "")
    date_info = date_info.replace("]", "")
    date_info = date_info.replace('"', '')
    date_info = date_info.replace('????', '1900')
    date_info = date_info.replace('??', '01')
    return date_info


def clean_round(round_info):
    round_info = round_info.replace("[Round ", "")
    round_info = round_info.replace("]", "")
    round_info = round_info.replace('"', '')
    return round_info


def clean_white(white_info):
    white_info = white_info.replace("[White ", "")
    white_info = white_info.replace("]", "")
    white_info = white_info.replace('"', '')
    white_info = white_info.replace('(wh)', '')
    return white_info


def clean_black(black_info):
    black_info = black_info.replace("[Black ", "")
    black_info = black_info.replace("]", "")
    black_info = black_info.replace('"', '')
    black_info = black_info.replace('(bl)', '')
    return black_info


def clean_result(result_info):
    result_info = result_info.replace("[Result ", "")
    result_info = result_info.replace("]", "")
    result_info = result_info.replace('"', '')
    if result_info in "1/2-1/2":
        result_info = "0"
    elif result_info in "1-0":
        result_info = "1"
    elif result_info in "0-1":
        result_info = "2"
    return result_info


def clean_rating(rating_info):
    rating_info = rating_info.replace("[WhiteElo ", "")
    rating_info = rating_info.replace("[BlackElo ", "")
    rating_info = rating_info.replace("]", "")
    rating_info = rating_info.replace('"', '')
    if not rating_info:
        rating_info = "0"
    return rating_info


def clean_ECO(ECO_info):
    ECO_info = ECO_info.replace("[ECO ", "")
    ECO_info = ECO_info.replace("]", "")
    ECO_info = ECO_info.replace('"', '')
    return ECO_info


def clean_moves(moves_info):
    white_moves = []
    black_moves = []
    for i in reversed(range(200)):
        move_number = str(i+1) + "."
        if move_number in moves_info:
            moves_info = moves_info.replace(move_number, " ")
        else:
            continue
    moves_info = moves_info.split()[:-1]
    for i in range(len(moves_info)):
        if i % 2 == 0:
            white_moves.append(moves_info[i])
        else:
            black_moves.append(moves_info[i])
    return white_moves, black_moves


def write_to_file(short_database_clean):
    game_string = ""
    for game in short_database_clean:
        game_string += " ; ".join(game[:-2]) + " ; " + ".".join(game[-2]) + " ; " + ".".join(game[-1]) + '\n'
    with open("formatted.csv", "w+") as f:
        f.write(game_string)


if __name__ == "__main__":
    file_path = sys.argv[1]
    short_database_gross = read_file_contents(file_path)
    short_database_clean = clean_short_database(short_database_gross)
    write_to_file(short_database_clean)
