# High-control mechanism

This bot is a chess bot created in Python using a built-in "chess" library. This bot is implemented using various min-max algorithms and an FSM structure that switches between multiple states:

1. Opening State
- Looks at how the opponent opens and reacts accordingly. This will be done using the chess library's "polyglot" function, which takes all of the possible openings and makes the proper move according to how the game opens. Once the opening has been handled (or for this iteration, once the engine makes four moves), the bot calculates their score based off of a weighted piece system and switches into another state.
- UPDATE: the new opening state is much more streamlined. Moves are read from the gm2001 book (located in the engines/engine_building directory), and when book moves are exhausted, the bot now transitions seamlessly into the midgame states.

2. Mid-Game Winning State

- If the user is winning, the bot will adopt a more aggressive mindset. They will be more willing to "trade" pieces with the opponent, knowing that they have an overall point advantage. They will also pursue moves that reach a favorable "endgame" state faster.

3. Mid-Game Not Winning State

- If the bot is either tied or losing, they will attempt to maneuver their way into a winning state. This will be done using the predictive "2 moves ahead" min-max algorithm with much less of an inclination to trade pieces.

4. Endgame State

- This state is reached when either player has less than or equal to 13 points (more on that below). In this case, the engine will be looking for ways to reach checkmate.

5. Killshot State

- This state is reached when the engine has twice as many points as the other player. From this state, the engine will aggressively look for a way to end the game, whether it be via tying or winning.

# Scoring System

The scoring system for the algorithm uses the following scores:

- Pawn: 1 point
- Knight/Bishop: 3 points
- Rook: 5 points
- Queen: 9 points

From this, a proper score can be calculated for the min-max algorithm.

# Lichess Connection
The bot is fully able to accept challenges and play games on the Lichess platform.
UPDATE: progress is being made to get the bot to challenge other bots automatically. This process is difficult because Lichess has removed the bot search functionality, so we will have to scrape the page for Bot names, and challenge them directly as friends.

# Dependencies/Configurations:

To operate this bot, the system requires python3, pip, backoff, and python-chess. Pip can be installed using the following command:
- sudo apt install python-pip (Linux)
- get-pip.py (Mac)
- python get-pip.py (Windows)

The package python-chess (0.24.1 is required) is installed in the Makefile using pip. The backoff package (1.7.1) is also installed in the Makefile using pip. Though this should implement everything necessary, check for potential further package installments under lichess-bot-master/requirements.txt for any potential further requirements.

