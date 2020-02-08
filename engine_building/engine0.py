#/usr/bin/env python3
# Engine 0 - totally random moves

import chess
import random

class Engine0:
	def __init__(self):
		pass
	def make_move(self, board):
		board.push(random.choice(list(board.legal_moves)))
