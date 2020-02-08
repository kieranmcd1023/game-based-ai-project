#!/usr/bin/env python3

import chess
import random
import time
from engine0 import Engine0 # totally random moves
from engine1 import Engine1 # always try to capture pieces

CPU_VS_CPU = True

if __name__ == '__main__':
	# Initialize engines
	e0 = Engine0()
	e1 = Engine1()

	# Initialize board
	board = chess.Board()

	# Game loop
	while not board.is_game_over():
		# Show board
		print('')
		print(board.unicode())
		print('')
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
		print('')
		print(board.unicode())
		print('')
		# Calculate bot move
		if board.is_game_over():
			break
		e1.make_move(board)

	print(board.unicode())
	print('Result: ', board.result())
	print('Number of full moves: ', board.fullmove_number)
