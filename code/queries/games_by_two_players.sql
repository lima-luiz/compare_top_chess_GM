SET @player1 = "%Alekhine%";
SET @player2 = "%Capablanca%";
SELECT * FROM chess_games WHERE (White LIKE @player1 AND Black LIKE @player2) OR (White LIKE @player2 AND Black LIKE @player1)