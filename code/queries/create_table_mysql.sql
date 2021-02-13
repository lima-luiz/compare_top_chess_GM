CREATE TABLE CHESS_GAMES (
	Event_name varchar(255),
    Site varchar(255),
    Game_date date,
    Match_round int,
    White varchar(255),
    Black varchar(255),
    Result int,
    White_ELO int,
    Black_ELO int,
    ECO varchar(12),
    White_moves varchar(600),
    Black_moves varchar(600)
);