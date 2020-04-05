#!/usr/bin/env python3

import chess
import random
import time
from high_level_strategy import ControlMechanism
from engine0 import Engine0 # totally random moves
from engine1 import Engine1 # always try to capture pieces
from engine2 import Engine2 # MinMax strategy

CPU_VS_CPU = True

def show_board(board):
	print('')
	print(board.unicode())
	print('')

if __name__ == '__main__':
	# Initialize control mechansim
	fsm = ControlMechanism(chess.BLACK)

	# Initialize engines
	e0 = Engine1() # White
	e1 = Engine2() # Black

	# Initialize board
	board = chess.Board()

	# Game loop
	while not board.is_game_over():
		# Show board
		show_board(board)

		if not CPU_VS_CPU:
			# Wait for human's move
			user_legal_moves = [board.san(x) for x in list(board.legal_moves)]
			print('Legal moves: ', user_legal_moves)
			print('Enter your move: ')
			user_move = str(input())
			while user_move not in user_legal_moves:
				print('Illegal move - enter another move: ')
				user_move = str(input())
			board.push_san(user_move)
		else:
			e0.make_move(board)

		show_board(board)

		# Calculate bot move
		if board.is_game_over():
			break
		fsm.make_move(board)

	show_board(board)
	print('Result: ', board.result())
	print('Number of full moves: ', board.fullmove_number)
