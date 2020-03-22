#!/usr/bin/env python3

import chess
import random
from engine2 import Engine2

if __name__ == '__main__':
	board = chess.Board()
	engine = Engine2()
	# Loop
	while True:
		# Get input
		inp = input()
		if not inp: continue
		line = inp.split()
#		print(line)
		# Parse input
		if line[0] == 'uci':
			print('uciok')
		elif line[0] == 'debug':
			continue
		elif line[0] == 'isready':
			print('readyok')
		elif line[0] == 'setoption':
			continue
		elif line[0] == 'register':
			continue
		elif line[0] == 'ucinewgame':
			print('isready')
		elif line[0] == 'position':
#			if line[1] == 'startpos':
#				board = chess.Board()
#			elif line[1] == 'fen':
#				print(0/0)
			board = chess.Board()
			if len(line) > 2 and line[2] == 'moves':
				for move in line[3:]:
					board.push(chess.Move.from_uci(move))
		elif line[0] == 'go':
			# Random
			#bestmove = chess.Move.uci(random.choice(list(board.legal_moves)))
			# Minimax
			engine.make_move(board)
			bestmove = board.peek()
			# Output best move
			#board.push(chess.Move.from_uci(bestmove))
			print('bestmove', bestmove)
		else:
			print('unknown command')
