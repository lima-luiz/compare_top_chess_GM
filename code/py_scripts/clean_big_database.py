import sys


GMs = ["Alekhine, A.", "Botvinnik, M.", "Capablanca, J.", "Fischer, R.", "Karpov, A.", "Kasparov, G.",
               "Kramnik, V.", "Lasker, E.", "Petrosian, T.", "Tal, M."]


def trasverse_file(file_path):
    summarized_data = []
    count = 0
    with open(file_path, 'r') as file:
        event = ""; site = ""; date = ""; round = ""; white = ""; black = ""
        result = ""; white_elo = ""; black_elo = ""; eco = ""; moves = ""
        current_game = [event, site, date, round, white, black, result, white_elo, black_elo, eco, moves]
        while True:
            line, summarized_data, file_over_flag = check_file_over(file, summarized_data, current_game)
            if file_over_flag: break
            current_game, summarized_data, count = read_current_game_data(line, current_game, count, summarized_data)
            print_periodic_log(current_game[4], count)
    return summarized_data


def check_file_over(file, summarized_data, current_game):
    try:
        line = file.readline()
        line = line.replace("\n"," ")
        file_over_flag = False
    except:
        line = ""
        summarized_data.append(current_game)
        file_over_flag = True
    return line, summarized_data, file_over_flag


def read_current_game_data(line, current_game, count, summarized_data):
    [event, site, date, round, white, black, result, white_elo, black_elo, eco, moves] = current_game
    if "[Event" in line:
        count += 1
        for player in GMs:
            if player in white or player in black:
                summarized_data.append(current_game)
        site = ""; date = ""; round = ""; white = ""; black = ""
        result = ""; white_elo = ""; black_elo = ""; eco = ""; moves = ""; event = line
    elif "[Site" in line:
        site = line
    elif "[Date" in line:
        date = line
    elif "[Round" in line:
        round = line
    elif '[White "' in line:
        white = line
    elif '[Black "' in line:
        black = line
    elif "[Result" in line:
        result = line
    elif "[WhiteElo" in line:
        white_elo = line
    elif "[BlackElo" in line:
        black_elo = line
    elif "[ECO" in line:
        eco = line
    else:
        moves += line
    current_game = [event, site, date, round, white, black, result, white_elo, black_elo, eco, moves]
    return current_game, summarized_data, count


def print_periodic_log(white, count):
    if count % 1000 == 0:
        print(count)
        print(white)


def write_summarized_file(summarized_data):
    with open("short_database.txt", 'w+') as file:
        for game in summarized_data:
            file.write(";".join(game))
            file.write("\n")


if __name__ == "__main__":
    file_path = sys.argv[1]
    summarized_data = trasverse_file(file_path)
    write_summarized_file(summarized_data)