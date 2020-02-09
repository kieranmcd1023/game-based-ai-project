#!/usr/bin/env python3
# Engine 1 - Greedy Algorithm

import chess
import random

class Engine1:
	def __init__(self):
		pass
	def make_move(self, board):
		# Random choices, unless a piece can be captured
		# Always capture a piece if possible
		capture_moves = [x for x in list(board.legal_moves) if board.is_capture(x)]
		if capture_moves:
			board.push(random.choice(capture_moves))
		else:
			board.push(random.choice(list(board.legal_moves)))
